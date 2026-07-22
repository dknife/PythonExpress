// 알짜 파이썬 — 코드 실행 워커 (Pyodide / CPython WebAssembly)
//
// 메인 스레드가 아니라 워커에서 돌리는 이유:
//   1) 무한 루프를 만들어도 페이지가 얼지 않는다
//   2) terminate()로 실행을 중단할 수 있다 (파이썬 안에서는 멈출 방법이 없다)
//
// input()은 대화형으로 받을 수 없다. 그러려면 SharedArrayBuffer가 필요하고,
// 그건 COOP/COEP 헤더를 요구하는데 GitHub Pages는 헤더를 설정할 수 없다.
// 그래서 실행 전에 '입력값' 상자로 미리 받아 둔 줄을 하나씩 돌려준다.
//
// 이 파일은 반드시 모듈 워커로 띄워야 한다 -- new Worker(url, {type:'module'}).
// Pyodide 314는 클래식 워커를 더 이상 지원하지 않는다
// ("Classic web workers are not supported"). 그래서 importScripts가 아니라
// ESM import를 쓴다.

// 정적 import는 URL에 변수를 못 쓰므로 아래 두 경로를 함께 고쳐야 한다.
import { loadPyodide } from 'https://cdn.jsdelivr.net/pyodide/v314.0.2/full/pyodide.mjs';
var PYODIDE_URL = 'https://cdn.jsdelivr.net/pyodide/v314.0.2/full/';

var py = null;

// input() 대체와 matplotlib 그림 수집기를 메인 네임스페이스에 심어 둔다.
var PRELUDE = [
  'import builtins, sys',
  '',
  'def _algja_stdin(text):',
  '    lines = text.split("\\n") if text else []',
  '    while lines and lines[-1] == "":',
  '        lines.pop()',
  '    it = iter(lines)',
  '    def _input(prompt=""):',
  '        try:',
  '            line = next(it)',
  '        except StopIteration:',
  '            raise EOFError(',
  '                "입력값이 모자랍니다. 창의 \'입력값\' 상자에 "',
  '                "필요한 만큼 한 줄에 하나씩 적어 주세요."',
  '            ) from None',
  '        if prompt:',
  '            print(prompt, end="")',
  '        print(line)',
  '        return line',
  '    builtins.input = _input',
  '',
  'def _algja_figs():',
  '    mod = sys.modules.get("matplotlib.pyplot")',
  '    if mod is None:',
  '        return []',
  '    import base64, io',
  '    out = []',
  '    for n in mod.get_fignums():',
  '        buf = io.BytesIO()',
  '        mod.figure(n).savefig(buf, format="png", dpi=110, bbox_inches="tight")',
  '        out.append(base64.b64encode(buf.getvalue()).decode())',
  '    mod.close("all")',
  '    return out',
  ''
].join('\n');

function post(t, m) {
  self.postMessage({ t: t, m: m });
}

async function ensurePyodide() {
  if (py) return py;
  post('status', '파이썬을 내려받는 중입니다 — 처음 한 번만 걸립니다');
  py = await loadPyodide({ indexURL: PYODIDE_URL });
  py.setStdout({ batched: function (s) { post('out', s + '\n'); } });
  py.setStderr({ batched: function (s) { post('err', s + '\n'); } });
  await py.runPythonAsync(PRELUDE);
  return py;
}

self.onmessage = async function (ev) {
  var code = ev.data.code || '';
  var stdin = ev.data.stdin || '';
  var ns = null;
  try {
    var p = await ensurePyodide();

    post('status', '필요한 패키지를 확인하는 중…');
    await p.loadPackagesFromImports(code);

    // matplotlib은 화면이 없으므로 Agg로 그린 뒤 PNG로 뽑아 보여 준다.
    // (plt.show()는 Agg에서 아무 일도 하지 않는다)
    try {
      await p.runPythonAsync(
        'import sys\n' +
        'if "matplotlib" in sys.modules or True:\n' +
        '    try:\n' +
        '        import matplotlib\n' +
        '        matplotlib.use("Agg")\n' +
        '    except ImportError:\n' +
        '        pass\n');
    } catch (e) { /* matplotlib이 없으면 그냥 넘어간다 */ }

    p.globals.set('_algja_stdin_text', stdin);
    await p.runPythonAsync('_algja_stdin(_algja_stdin_text)');

    // 실행할 때마다 빈 이름공간을 준다.
    // __name__을 "__main__"으로 두어야 if __name__ == "__main__": 블록이 돈다.
    ns = p.runPython('dict(__name__="__main__")');

    post('status', '실행 중…');
    await p.runPythonAsync(code, { globals: ns });

    var figs = await p.runPythonAsync('_algja_figs()');
    var list = figs && figs.toJs ? figs.toJs() : [];
    if (figs && figs.destroy) figs.destroy();

    post('figs', list);
    post('done', '');
  } catch (err) {
    post('err', (err && err.message ? err.message : String(err)) + '\n');
    post('done', '');
  } finally {
    if (ns && ns.destroy) ns.destroy();
  }
};

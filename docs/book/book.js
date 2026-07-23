// 알짜 파이썬 웹 본문 — 인터랙션 (DESIGN.md 기반)
// 1) 스크롤 리빌  2) 그림 클릭 → 별도 창 확대 보기  3) 코드 복사 버튼

// ---- 1) 스크롤 리빌 ----
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var targets = document.querySelectorAll(
    '.content figure.fig, .content .box, .content .listing, ' +
    '.content .table-wrap, .content pre.line-numbers, ' +
    '.content pre.pyout, .content pre.termout, .cover-wrap');
  targets.forEach(function (el) { el.classList.add('reveal'); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -5% 0px' });
  targets.forEach(function (el) { io.observe(el); });
})();

// ---- 1.5) 사이드바 링크 클릭 시 모바일 목차 서랍 닫기 ----
// 절(#anchor) 링크는 페이지 이동이 없어 서랍이 열린 채 본문을 가리는 문제 방지
(function () {
  document.querySelectorAll('.sidebar a').forEach(function (a) {
    a.addEventListener('click', function () {
      document.body.classList.remove('nav-open');
    });
  });
})();

// ---- 1.6) 접힌 박스(details)로의 앵커 이동 시 자동 펼침 ----
// 사이드바에서 "연습문제"를 누르면 접힌 상태로 이동해 보이지 않는 문제 방지
(function () {
  function openTarget() {
    var id = location.hash.replace('#', '');
    if (!id) return;
    var el = document.getElementById(id);
    if (el && el.tagName === 'DETAILS') el.open = true;
  }
  window.addEventListener('hashchange', openTarget);
  openTarget();
})();

// ---- 2) 그림 클릭 → 별도 창 확대 ----
(function () {
  var imgs = document.querySelectorAll(
    '.content img.tikz, .content img.gfx, .content img.shot, ' +
    '.content img.chapfig, .content img.cover');
  imgs.forEach(function (img) {
    img.classList.add('zoomable');
    img.title = '클릭하면 새 창에서 크게 볼 수 있습니다';
    img.addEventListener('click', function () {
      var src = img.getAttribute('src');
      var w = Math.min(window.screen.availWidth, 1280);
      var h = Math.min(window.screen.availHeight, 900);
      window.open('viewer.html?src=' + encodeURIComponent(src),
        'figviewer', 'width=' + w + ',height=' + h +
        ',menubar=no,toolbar=no,location=no,status=no');
    });
  });
})();

// ---- 3) 코드 복사 · 실행 버튼 ----
(function () {
  var COPY_ICON =
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" ' +
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" ' +
    'stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" ' +
    'rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 ' +
    '2-2h9a2 2 0 0 1 2 2v1"></path></svg>';
  var OK_ICON =
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" ' +
    'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" ' +
    'stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';

  var RUN_ICON =
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" ' +
    'stroke="none"><polygon points="6 3 21 12 6 21"></polygon></svg>';

  document.querySelectorAll('.content pre.line-numbers').forEach(function (pre) {
    var codeEl = pre.querySelector('code');
    if (!codeEl) return;
    var wrap = document.createElement('div');
    wrap.className = 'code-wrap';
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);
    var bar = document.createElement('div');
    bar.className = 'code-actions';
    wrap.appendChild(bar);

    var runBtn = document.createElement('button');
    runBtn.className = 'copy-btn run-btn';
    runBtn.type = 'button';
    runBtn.title = '이 코드를 창에서 고쳐 가며 실행해 봅니다';
    runBtn.innerHTML = RUN_ICON + '<span>실행</span>';
    bar.appendChild(runBtn);
    runBtn.addEventListener('click', function () {
      window.algjaRunner.open(codeEl.textContent.replace(/\n$/, ''));
    });

    var btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.title = '코드 복사 (행번호 제외)';
    btn.innerHTML = COPY_ICON + '<span>복사</span>';
    bar.appendChild(btn);
    btn.addEventListener('click', function () {
      // Prism 토큰만 담긴 code 요소의 textContent에는 행번호가 포함되지 않음
      var text = codeEl.textContent.replace(/\n$/, '');
      function done(ok) {
        btn.innerHTML = ok ? OK_ICON + '<span>복사됨</span>'
                           : COPY_ICON + '<span>실패</span>';
        btn.classList.toggle('ok', ok);
        setTimeout(function () {
          btn.innerHTML = COPY_ICON + '<span>복사</span>';
          btn.classList.remove('ok');
        }, 1600);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(
          function () { done(true); }, function () { done(false); });
      } else {
        var ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        var ok = false;
        try { ok = document.execCommand('copy'); } catch (e) {}
        document.body.removeChild(ta);
        done(ok);
      }
    });
  });
})();

// ---- 4) 코드 실행 창 (Pyodide 워커) ----
// 브라우저는 방문자 PC의 파이썬을 실행할 수 없다(샌드박스). 대신 CPython을
// WebAssembly로 포팅한 Pyodide를 워커에서 돌린다. 설치가 필요 없고 결과는
// 실제 CPython 3.14와 같다. 다만 화면·서버가 필요한 모듈은 쓸 수 없다.
window.algjaRunner = (function () {
  var RUN_TIMEOUT_MS = 20000;
  var UNSUPPORTED = [
    [/^\s*(?:import|from)\s+turtle\b/m, 'turtle',
     '거북이 그래픽은 별도의 창을 띄우는 기능이라 브라우저 안에서는 동작하지 않습니다.'],
    [/^\s*(?:import|from)\s+tkinter\b/m, 'tkinter',
     'tkinter GUI는 운영체제의 창이 필요해 브라우저 안에서는 동작하지 않습니다.'],
    [/^\s*(?:import|from)\s+flask\b/mi, 'Flask',
     'Flask는 웹 서버를 띄워 포트를 여는 프로그램이라 브라우저 안에서는 동작하지 않습니다.']
  ];

  var dlg = null, ui = {}, worker = null, timer = null, original = '';
  // 워커는 창을 닫아도 살려 둔다 -- 파이썬을 한 번만 올리기 위해서다.
  // ready: 파이썬이 이미 올라와 있는가, busy: 지금 실행 중인가
  var ready = false, busy = false, startedAt = 0;

  function build() {
    dlg = document.createElement('dialog');
    dlg.className = 'runner';
    dlg.setAttribute('aria-label', '코드 실행');
    dlg.innerHTML =
      '<div class="runner-head">' +
        '<span class="runner-title">코드 실행</span>' +
        '<span class="runner-hint">Ctrl+Enter 실행 · Esc 닫기</span>' +
        '<button type="button" class="runner-close" aria-label="닫기">&#10005;</button>' +
      '</div>' +
      '<textarea class="runner-code" spellcheck="false" ' +
        'aria-label="파이썬 코드"></textarea>' +
      '<div class="runner-stdin-wrap" hidden>' +
        '<label class="runner-label" for="algja-stdin">입력값' +
        '<span> — input() 이 읽어 갈 값을 한 줄에 하나씩</span></label>' +
        '<textarea id="algja-stdin" class="runner-stdin" rows="2" ' +
          'spellcheck="false"></textarea>' +
      '</div>' +
      '<div class="runner-bar">' +
        '<button type="button" class="runner-run">실행</button>' +
        '<button type="button" class="runner-stop" hidden>중지</button>' +
        '<button type="button" class="runner-reset">원래 코드로</button>' +
        '<span class="runner-status"></span>' +
      '</div>' +
      '<pre class="runner-out" aria-live="polite"></pre>' +
      '<div class="runner-figs"></div>';
    document.body.appendChild(dlg);

    ui.code = dlg.querySelector('.runner-code');
    ui.stdinWrap = dlg.querySelector('.runner-stdin-wrap');
    ui.stdin = dlg.querySelector('.runner-stdin');
    ui.run = dlg.querySelector('.runner-run');
    ui.stop = dlg.querySelector('.runner-stop');
    ui.reset = dlg.querySelector('.runner-reset');
    ui.status = dlg.querySelector('.runner-status');
    ui.out = dlg.querySelector('.runner-out');
    ui.figs = dlg.querySelector('.runner-figs');

    dlg.querySelector('.runner-close').addEventListener('click', close);
    // 창을 닫을 때는 돌고 있는 것만 끊는다. 놀고 있는 워커는 그대로 두어야
    // 다음에 열었을 때 파이썬을 다시 내려받지 않는다.
    dlg.addEventListener('close', function () { if (busy) abortRun(); });
    ui.run.addEventListener('click', run);
    ui.stop.addEventListener('click', function () {
      abortRun();
      setStatus('중지했습니다.');
    });
    ui.reset.addEventListener('click', function () {
      ui.code.value = original;
      syncStdinBox();
      ui.code.focus();
    });

    // 파이썬 책이니 Tab은 4칸 들여쓰기로 넣는다 (포커스 이동이 아니라)
    ui.code.addEventListener('keydown', function (e) {
      if (e.key === 'Tab') {
        e.preventDefault();
        var s = ui.code.selectionStart, t = ui.code.selectionEnd;
        ui.code.value = ui.code.value.slice(0, s) + '    ' + ui.code.value.slice(t);
        ui.code.selectionStart = ui.code.selectionEnd = s + 4;
      } else if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
        e.preventDefault();
        run();
      }
    });
    ui.code.addEventListener('input', syncStdinBox);
  }

  function syncStdinBox() {
    ui.stdinWrap.hidden = !/\binput\s*\(/.test(ui.code.value);
  }

  function setStatus(msg) { ui.status.textContent = msg || ''; }

  function append(cls, text) {
    var span = document.createElement('span');
    if (cls) span.className = cls;
    span.textContent = text;
    ui.out.appendChild(span);
    ui.out.scrollTop = ui.out.scrollHeight;
  }

  // 실행 하나가 끝났을 때 -- UI만 되돌리고 워커는 살려 둔다.
  // 워커를 죽이면 다음 실행 때 파이썬을 처음부터 다시 올려야 한다.
  function endRun() {
    if (timer) { clearTimeout(timer); timer = null; }
    busy = false;
    ui.run.disabled = false;
    ui.stop.hidden = true;
  }

  // 중지·시간 초과 -- 돌고 있는 파이썬을 멈출 방법은 워커를 죽이는 것뿐이다.
  // 이 경우에만 다음 실행이 다시 준비 과정을 거친다.
  function abortRun() {
    if (worker) { worker.terminate(); worker = null; }
    ready = false;
    endRun();
  }


  function ensureWorker() {
    if (worker) return worker;
    // Pyodide 314는 모듈 워커만 지원한다 (클래식 워커 불가)
    worker = new Worker('pyrunner.js', { type: 'module' });
    worker.onmessage = function (ev) {
      var t = ev.data.t, m = ev.data.m;
      if (t === 'ack') { /* 수신 확인 신호 -- 따로 할 일은 없다 */ }
      else if (t === 'status') { setStatus(m); }
      else if (t === 'out') { append(null, m); }
      else if (t === 'err') { append('err', m); }
      else if (t === 'figs') {
        (m || []).forEach(function (b64) {
          var img = document.createElement('img');
          img.src = 'data:image/png;base64,' + b64;
          img.alt = '실행 결과 그래프';
          ui.figs.appendChild(img);
        });
      } else if (t === 'done') {
        var secs = ((Date.now() - startedAt) / 1000).toFixed(1);
        ready = true;
        endRun();
        if (!ui.out.textContent && !ui.figs.childNodes.length) {
          append('muted', '(출력 없음)\n');
        }
        setStatus('완료 — ' + secs + '초');
      }
    };
    worker.onerror = function (e) {
      append('err', '실행기를 불러오지 못했습니다: ' + (e.message || e) + '\n');
      abortRun();
      setStatus('오류');
    };
    return worker;
  }

  function run() {
    if (busy) return;
    var code = ui.code.value;
    ui.out.textContent = '';
    ui.figs.innerHTML = '';

    for (var i = 0; i < UNSUPPORTED.length; i++) {
      if (UNSUPPORTED[i][0].test(code)) {
        append('warn',
          UNSUPPORTED[i][1] + ' — ' + UNSUPPORTED[i][2] + '\n\n' +
          '이 코드는 [복사] 버튼으로 가져가 내 컴퓨터에 설치한 파이썬에서 ' +
          '실행해 주세요.\n');
        setStatus('브라우저에서 실행할 수 없는 코드입니다.');
        return;
      }
    }

    busy = true;
    ui.run.disabled = true;
    ui.stop.hidden = false;
    setStatus(ready ? '실행 중…' : '준비 중…');

    startedAt = Date.now();
    ensureWorker().postMessage({ code: code, stdin: ui.stdin.value });

    timer = setTimeout(function () {
      abortRun();
      append('warn',
        '\n실행이 ' + (RUN_TIMEOUT_MS / 1000) + '초를 넘겨 중지했습니다. ' +
        '끝나지 않는 반복문이 있는지 확인해 보세요.\n' +
        '(멈추려면 파이썬을 내려야 해서 다음 실행은 준비 시간이 다시 걸립니다)\n');
      setStatus('시간 초과로 중지');
    }, RUN_TIMEOUT_MS);
  }

  function open(code) {
    if (!dlg) build();
    if (busy) abortRun();
    original = code;
    ui.code.value = code;
    ui.out.textContent = '';
    ui.figs.innerHTML = '';
    setStatus('');
    syncStdinBox();
    dlg.showModal();
    ui.code.focus();
    ui.code.setSelectionRange(0, 0);
  }

  function close() { if (dlg && dlg.open) dlg.close(); }

  return { open: open, close: close };
})();

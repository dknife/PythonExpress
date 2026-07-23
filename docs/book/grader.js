// 알짜 파이썬 — 연습문제 답안 작성 + 자동 채점 (1단계: 순수 클라이언트)
//
// 문제 유형 (docs/book/ex/chNN.json 스펙):
//   output  — "출력 결과를 쓰시오": 학생 답안 텍스트를 기대 출력과 정규화 비교
//   code    — "프로그램을 작성하시오": Pyodide 워커에서 실행해 테스트별
//             stdin -> 기대 stdout 비교 (pyrunner.js 재사용)
//   short   — 단답/고르기: 토큰 집합 비교
//   keyword — 서술형: 핵심 개념(동의어 그룹)이 몇 개 언급됐는지로 Pass/Fail
//
// 채점 결과와 답안은 localStorage에만 저장된다 (서버 전송 없음).
(function () {
  var m = location.pathname.match(/ch(\d\d)\.html$/);
  if (!m) return;
  var chap = m[1];
  var box = document.querySelector('.box.exercise');
  if (!box) return;

  var STORE = 'algja-ex-ch' + chap;

  function loadAll() {
    try { return JSON.parse(localStorage.getItem(STORE)) || {}; }
    catch (e) { return {}; }
  }
  function saveAll(st) {
    try { localStorage.setItem(STORE, JSON.stringify(st)); } catch (e) {}
  }

  // ---- 출력 비교 정규화: CR 제거, 각 줄 끝 공백 제거, 앞뒤 빈 줄 제거 ----
  function normOut(s) {
    return String(s || '').replace(/\r/g, '')
      .split('\n').map(function (l) { return l.replace(/\s+$/, ''); })
      .join('\n').replace(/^\n+/, '').replace(/\n+$/, '');
  }
  // 서술형/단답 매칭용: 소문자화 + 공백 제거
  function normText(s) {
    return String(s || '').toLowerCase().replace(/\s+/g, '');
  }

  // ---- 코드 채점용 Pyodide 워커 (pyrunner.js 재사용) ----
  var worker = null;
  function runPython(code, stdin) {
    return new Promise(function (resolve) {
      if (!worker) worker = new Worker('pyrunner.js', { type: 'module' });
      var out = '', err = '';
      var timer = setTimeout(function () {
        cleanup();
        if (worker) { worker.terminate(); worker = null; }
        resolve({ out: out, err: err + '(시간 초과 — 무한 루프인지 확인하세요)\n' });
      }, 25000);
      function onmsg(ev) {
        var t = ev.data.t, msg = ev.data.m;
        if (t === 'out') out += msg;
        else if (t === 'err') err += msg;
        else if (t === 'done') { cleanup(); resolve({ out: out, err: err }); }
      }
      function cleanup() {
        clearTimeout(timer);
        if (worker) worker.removeEventListener('message', onmsg);
      }
      worker.addEventListener('message', onmsg);
      worker.postMessage({ code: code, stdin: stdin || '' });
    });
  }

  // ---- 채점기 ----
  function gradeOutput(spec, val) {
    var ok = normOut(val) === normOut(spec.expected);
    return { pass: ok, detail: ok ? '' : '기대한 출력과 다릅니다. 공백·줄바꿈까지 확인해 보세요.' };
  }

  function gradeShort(spec, val) {
    var mode = spec.match || 'set';
    if (mode === 'exact') {
      var ok = normText(val) === normText(spec.answers[0]);
      return { pass: ok, detail: '' };
    }
    var toks = String(val || '').toLowerCase()
      .split(/[\s,;()\/·]+/).filter(Boolean);
    var ans = spec.answers.map(function (a) { return String(a).toLowerCase(); });
    if (mode === 'any') {
      var hit = toks.some(function (t) { return ans.indexOf(t) >= 0; });
      return { pass: hit, detail: '' };
    }
    // set: 정답 집합과 정확히 일치해야 함
    var uniq = toks.filter(function (t, i) { return toks.indexOf(t) === i; });
    var okSet = uniq.length === ans.length &&
      uniq.every(function (t) { return ans.indexOf(t) >= 0; });
    return {
      pass: okSet,
      detail: okSet ? '' : '정답 개수는 ' + ans.length + '개입니다. 쉼표로 구분해 적어 주세요.'
    };
  }

  function gradeKeyword(spec, val) {
    var text = normText(val);
    if (text.length < (spec.min_length || 10)) {
      return { pass: false, detail: '답안이 너무 짧습니다. 문장으로 설명해 보세요.' };
    }
    var hitLabels = [], missLabels = [];
    spec.keywords.forEach(function (group) {
      var hit = group.some(function (kw) { return text.indexOf(normText(kw)) >= 0; });
      (hit ? hitLabels : missLabels).push(group[0]);
    });
    var need = spec.pass_min || spec.keywords.length;
    var pass = hitLabels.length >= need;
    var detail = '언급된 개념: ' + (hitLabels.join(', ') || '없음');
    if (!pass && missLabels.length) {
      detail += ' · 다뤄야 할 개념: ' + missLabels.join(', ');
    }
    detail += ' (' + hitLabels.length + '/' + need + ')';
    return { pass: pass, detail: detail };
  }

  // ---- 유사 채점 (코드 문제 2차 판정) ----
  // 출력 문구까지 똑같아야 통과하는 것은 지나치게 엄격하다. 여러 테스트의
  // 기대 출력을 겹쳐 보면 테스트마다 변하는 토큰이 곧 "핵심 정답"이고
  // (예: 학점 A/C/F), 변하지 않는 부분은 프롬프트·라벨(형식)이다.
  // 핵심 정답이 모두 있으면 형식이 달라도 통과시키되, 다른 테스트의
  // 정답이 섞여 있으면(모든 경우를 다 출력하는 꼼수) 탈락시킨다.
  function tokensOf(s) {
    var m = String(s || '').toLowerCase().match(/[a-z가-힣0-9_]+(?:\.[0-9]+)?/g);
    return m || [];
  }
  function tokenEq(a, b) {
    if (a === b) return true;
    var na = parseFloat(a), nb = parseFloat(b);
    if (isFinite(na) && isFinite(nb) &&
        /^[0-9.\-]+$/.test(a) && /^[0-9.\-]+$/.test(b)) {
      return Math.abs(na - nb) <= Math.abs(nb) * 1e-9 + 1e-9;
    }
    return false;
  }
  function hasToken(list, tok) {
    return list.some(function (t) { return tokenEq(t, tok); });
  }
  // 각 테스트의 핵심 토큰(keys)과 금지 토큰(anti: 다른 테스트의 핵심) 계산
  function deriveTestKeys(tests) {
    var tokLists = tests.map(function (t) { return tokensOf(t.expected); });
    var keys = tests.map(function (t, i) {
      var stdinToks = tokensOf(t.stdin || '');
      if (tests.length >= 2) {
        // 모든 테스트에 공통인 토큰 = 형식(템플릿), 나머지 = 정답 후보
        return tokLists[i].filter(function (tok) {
          var inAll = tokLists.every(function (lst) { return hasToken(lst, tok); });
          return !inAll && !hasToken(stdinToks, tok);
        });
      }
      // 테스트가 하나뿐이면 변별할 기준이 없으므로 숫자 토큰만 핵심으로 본다
      return tokLists[i].filter(function (tok) {
        return /^[0-9.\-]+$/.test(tok) && isFinite(parseFloat(tok)) &&
               !hasToken(stdinToks, tok);
      });
    });
    var anti = keys.map(function (k, i) {
      var others = [];
      keys.forEach(function (k2, j) {
        if (j === i) return;
        k2.forEach(function (tok) {
          if (!hasToken(k, tok)) others.push(tok);
        });
      });
      return others;
    });
    return { keys: keys, anti: anti };
  }
  function looseOk(gotText, keys, anti) {
    if (!keys.length) return false;      // 핵심을 못 뽑으면 완전 일치만 인정
    var got = tokensOf(gotText);
    var allKeys = keys.every(function (tok) { return hasToken(got, tok); });
    var noAnti = anti.every(function (tok) { return !hasToken(got, tok); });
    return allKeys && noAnti;
  }

  function gradeCode(spec, code, ui) {
    if (!normOut(code)) {
      return Promise.resolve({ pass: false, detail: '코드를 입력해 주세요.' });
    }
    var tests = spec.tests || [];
    var derived = deriveTestKeys(tests);
    var results = [];
    var chain = Promise.resolve();
    tests.forEach(function (t, i) {
      chain = chain.then(function () {
        ui.setStatus('테스트 ' + (i + 1) + '/' + tests.length + ' 실행 중…');
        return runPython(code, t.stdin || '').then(function (r) {
          var got = normOut(r.out);
          var exact = !r.err && got === normOut(t.expected);
          var loose = !exact && !r.err &&
                      looseOk(got, derived.keys[i], derived.anti[i]);
          results.push({ i: i + 1, ok: exact || loose, loose: loose,
                         stdin: t.stdin || '',
                         expected: t.expected, got: r.out, err: r.err,
                         keys: derived.keys[i] });
        });
      });
    });
    return chain.then(function () {
      var failed = results.filter(function (r) { return !r.ok; });
      if (!failed.length) {
        var anyLoose = results.some(function (r) { return r.loose; });
        return { pass: true, detail: '테스트 ' + results.length + '개 모두 통과' +
                 (anyLoose ? ' (핵심 결과 일치 — 출력 형식은 자유)' : '') };
      }
      var f = failed[0];
      var lines = ['테스트 ' + results.length + '개 중 ' +
                   (results.length - failed.length) + '개 통과'];
      lines.push('― 실패한 테스트 ' + f.i +
                 (f.stdin ? ' (입력값: ' + f.stdin.trim().replace(/\n/g, ', ') + ')' : ''));
      if (f.err) lines.push('오류:\n' + f.err.trim());
      else {
        lines.push('기대 출력:\n' + normOut(f.expected) +
                   '\n실제 출력:\n' + (normOut(f.got) || '(출력 없음)'));
        if (f.keys && f.keys.length) {
          lines.push('※ 출력 문구가 똑같지 않아도 핵심 결과(' +
                     f.keys.join(', ') + ')가 담겨 있으면 통과합니다.');
        }
      }
      return { pass: false, detail: lines.join('\n') };
    });
  }
  // 단위 테스트용 노출 (페이지 동작에는 영향 없음)
  try {
    window._algjaLoose = { tokensOf: tokensOf, deriveTestKeys: deriveTestKeys,
                           looseOk: looseOk };
  } catch (e) {}

  // ---- UI ----
  var TYPE_LABEL = { output: '출력 예상', code: '코드 작성', short: '단답',
                     keyword: '서술 (키워드 채점)' };

  function buildWidget(li, prob, state, onGraded) {
    var w = document.createElement('div');
    w.className = 'ex-widget';
    var isCode = prob.type === 'code';
    var isLong = isCode || prob.type === 'output' || prob.type === 'keyword';
    w.innerHTML =
      '<div class="ex-head">' +
        '<span class="ex-type">' + (TYPE_LABEL[prob.type] || '자동 채점') + '</span>' +
        '<span class="ex-state"></span>' +
      '</div>' +
      (isLong
        ? '<textarea class="ex-ans' + (isCode || prob.type === 'output' ? ' mono' : '') +
          '" rows="' + (isCode ? 8 : 3) + '" spellcheck="false" placeholder="' +
          (isCode ? '여기에 파이썬 코드를 작성하세요'
                  : prob.type === 'output' ? '예상 출력을 그대로 적어 보세요'
                  : '자신의 말로 설명해 보세요') + '"></textarea>'
        : '<input class="ex-ans" type="text" spellcheck="false" placeholder="답을 입력하세요">') +
      '<div class="ex-bar">' +
        '<button type="button" class="ex-grade">채점</button>' +
        '<span class="ex-status"></span>' +
      '</div>' +
      '<div class="ex-result" hidden></div>';
    li.appendChild(w);

    var ans = w.querySelector('.ex-ans');
    var stateEl = w.querySelector('.ex-state');
    var statusEl = w.querySelector('.ex-status');
    var resultEl = w.querySelector('.ex-result');
    var btn = w.querySelector('.ex-grade');

    // 코드 입력창에서 Tab -> 스페이스 4칸
    if (isCode) {
      ans.addEventListener('keydown', function (e) {
        if (e.key === 'Tab') {
          e.preventDefault();
          var s = ans.selectionStart;
          ans.value = ans.value.slice(0, s) + '    ' + ans.value.slice(ans.selectionEnd);
          ans.selectionStart = ans.selectionEnd = s + 4;
        }
      });
    }

    function setBadge(st) {
      stateEl.textContent = st === 'pass' ? 'Pass' : st === 'fail' ? 'Fail' : '';
      stateEl.className = 'ex-state' + (st ? ' ' + st : '');
    }
    if (state) {
      if (state.a) ans.value = state.a;
      setBadge(state.p);
    }

    var ui = { setStatus: function (msg) { statusEl.textContent = msg || ''; } };

    btn.addEventListener('click', function () {
      btn.disabled = true;
      resultEl.hidden = true;
      var val = ans.value;
      var done = function (r) {
        btn.disabled = false;
        ui.setStatus('');
        setBadge(r.pass ? 'pass' : 'fail');
        if (r.detail) {
          resultEl.textContent = r.detail;
          resultEl.hidden = false;
        }
        onGraded(prob.n, { p: r.pass ? 'pass' : 'fail', a: val });
      };
      if (prob.type === 'code') gradeCode(prob, val, ui).then(done);
      else if (prob.type === 'output') done(gradeOutput(prob, val));
      else if (prob.type === 'short') done(gradeShort(prob, val));
      else if (prob.type === 'keyword') done(gradeKeyword(prob, val));
      else { btn.disabled = false; }
    });
  }

  // ---- 초기화 ----
  fetch('ex/ch' + chap + '.json')
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (spec) {
      if (!spec || !spec.problems || !spec.problems.length) return;
      var state = loadAll();
      var byN = {};
      spec.problems.forEach(function (p) { byN[p.n] = p; });

      var total = spec.problems.length;
      var head = box.querySelector('.box-head');
      var score = document.createElement('span');
      score.className = 'ex-score';
      if (head) head.appendChild(score);

      function refreshScore() {
        var passed = spec.problems.filter(function (p) {
          return state[p.n] && state[p.n].p === 'pass';
        }).length;
        score.textContent = '자동 채점 ' + passed + '/' + total + ' 통과';
        score.classList.toggle('all', passed === total);
      }
      function onGraded(n, st) {
        state[n] = st;
        saveAll(state);
        refreshScore();
      }

      box.querySelectorAll('li.ex-item').forEach(function (li) {
        var n = parseInt(li.getAttribute('data-ex'), 10);
        if (byN[n]) buildWidget(li, byN[n], state[n], onGraded);
      });
      refreshScore();
    })
    .catch(function () { /* 스펙 없는 장 — 조용히 무시 */ });
})();

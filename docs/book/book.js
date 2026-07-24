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
// turtle은 예외 -- 워커의 가짜 turtle 모듈이 그리기 명령을 기록해 보내면
// 여기서 캔버스에 거북이 애니메이션으로 재생한다(시뮬레이터).
window.algjaRunner = (function () {
  var RUN_TIMEOUT_MS = 20000;
  var UNSUPPORTED = [
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
    dlg.addEventListener('close', function () {
      if (busy) abortRun();
      stopTurtle();
    });
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

  // ---- 터틀 그래픽 시뮬레이터 (재생기) ----
  // 워커가 보낸 그리기 명령을 캔버스 두 장(그림 + 거북이 커서)에 재생한다.
  var turtleAnim = null;

  function stopTurtle() {
    if (turtleAnim) { cancelAnimationFrame(turtleAnim.raf); turtleAnim = null; }
  }

  function renderTurtle(json) {
    var data;
    try { data = JSON.parse(json); } catch (e) { return; }
    var cmds = data.cmds || [];
    var cursors = data.cursors || [];
    if (!cmds.length) return;
    stopTurtle();

    // 잉크가 닿는 영역을 재서 캔버스에 맞게 축척·중심을 정한다
    var minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    function grow(x, y, pad) {
      if (x - pad < minX) minX = x - pad;
      if (x + pad > maxX) maxX = x + pad;
      if (y - pad < minY) minY = y - pad;
      if (y + pad > maxY) maxY = y + pad;
    }
    cmds.forEach(function (c) {
      if (c.op === 'seg' && c.p) { grow(c.x1, c.y1, c.w); grow(c.x2, c.y2, c.w); }
      else if (c.op === 'dot') grow(c.x, c.y, c.s / 2);
      else if (c.op === 'stamp') grow(c.x, c.y, 12);
      else if (c.op === 'write') grow(c.x, c.y, 30);
      else if (c.op === 'fill') {
        c.pts.forEach(function (p) { grow(p[0], p[1], 0); });
      }
    });
    cursors.forEach(function (c) { grow(c.x, c.y, 14); });
    if (minX > maxX) { minX = minY = -100; maxX = maxY = 100; }

    var W = 560;
    var bw = Math.max(maxX - minX, 10), bh = Math.max(maxY - minY, 10);
    var H = Math.max(240, Math.min(460, Math.round(W * bh / bw)));
    var MARGIN = 24;
    var scale = Math.min(1, (W - MARGIN * 2) / bw, (H - MARGIN * 2) / bh);
    var cx = (minX + maxX) / 2, cy = (minY + maxY) / 2;
    function tx(x) { return W / 2 + (x - cx) * scale; }
    function ty(y) { return H / 2 - (y - cy) * scale; }  // 터틀 y축은 위가 +

    var wrap = document.createElement('div');
    wrap.className = 'turtle-wrap';
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var scene = document.createElement('canvas');
    var over = document.createElement('canvas');
    over.className = 'turtle-over';
    [scene, over].forEach(function (cv) {
      cv.width = Math.round(W * dpr);
      cv.height = Math.round(H * dpr);
    });
    wrap.appendChild(scene);
    wrap.appendChild(over);
    var note = document.createElement('div');
    note.className = 'turtle-note';
    note.textContent =
      '터틀 그래픽 시뮬레이터 — 내 컴퓨터의 파이썬에서는 별도의 창이 열립니다';
    ui.figs.appendChild(wrap);
    ui.figs.appendChild(note);

    var ctx = scene.getContext('2d');
    var octx = over.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    octx.setTransform(dpr, 0, 0, dpr, 0, 0);

    var bg = '#ffffff';
    var speed = 3;

    function paintBg() {
      ctx.fillStyle = bg;
      ctx.fillRect(0, 0, W, H);
    }

    function drawSeg(c) {
      if (!c.p || (c.x1 === c.x2 && c.y1 === c.y2)) return;
      ctx.beginPath();
      ctx.moveTo(tx(c.x1), ty(c.y1));
      ctx.lineTo(tx(c.x2), ty(c.y2));
      ctx.strokeStyle = c.c;
      ctx.lineWidth = Math.max(1, c.w * scale);
      ctx.lineCap = 'round';
      ctx.stroke();
    }

    // 거북이 커서(작은 화살촉). 터틀 각도는 반시계 +이고 화면 y는 아래가 +
    function drawShape(g, x, y, h, color) {
      g.save();
      g.translate(tx(x), ty(y));
      g.rotate(-h * Math.PI / 180);
      g.beginPath();
      g.moveTo(11, 0); g.lineTo(-5, 6); g.lineTo(-2, 0); g.lineTo(-5, -6);
      g.closePath();
      g.globalAlpha = 0.9;
      g.fillStyle = color || '#222';
      g.fill();
      g.restore();
    }

    function applyOp(c, idx) {
      if (c.op === 'bg') { bg = c.c; redraw(idx); }
      else if (c.op === 'clear') { paintBg(); }
      else if (c.op === 'speed') { speed = c.v; }
      else if (c.op === 'dot') {
        ctx.beginPath();
        ctx.arc(tx(c.x), ty(c.y), Math.max(1, c.s * scale / 2), 0, Math.PI * 2);
        ctx.fillStyle = c.c;
        ctx.fill();
      } else if (c.op === 'fill') {
        ctx.beginPath();
        c.pts.forEach(function (p, i) {
          if (i) ctx.lineTo(tx(p[0]), ty(p[1]));
          else ctx.moveTo(tx(p[0]), ty(p[1]));
        });
        ctx.closePath();
        ctx.fillStyle = c.c;
        ctx.fill();
        // 채우기가 이미 그린 윤곽선을 덮으므로 윤곽선을 한 번 더 그린다
        for (var i = c.f; i < idx; i++) {
          if (cmds[i].op === 'seg') drawSeg(cmds[i]);
        }
      } else if (c.op === 'write') {
        var style = /italic/.test(c.f[2]) ? 'italic ' : '';
        if (/bold/.test(c.f[2])) style += 'bold ';
        ctx.font = style + Math.max(7, Math.round(c.f[1] * scale * 1.33)) +
          'px "' + c.f[0] + '", sans-serif';
        ctx.textAlign = c.a === 'center' ? 'center'
          : (c.a === 'right' ? 'right' : 'left');
        ctx.textBaseline = 'bottom';
        ctx.fillStyle = c.c;
        ctx.fillText(c.t, tx(c.x), ty(c.y));
      } else if (c.op === 'stamp') {
        drawShape(ctx, c.x, c.y, c.h, c.c);
      }
    }

    // 배경색이 중간에 바뀌면 새 배경 위에 지금까지의 그림을 다시 그린다
    function redraw(upto) {
      paintBg();
      var start = 0, i;
      for (i = 0; i < upto; i++) if (cmds[i].op === 'clear') start = i + 1;
      for (i = start; i < upto; i++) {
        var c = cmds[i];
        if (c.op === 'seg') drawSeg(c);
        else if (c.op !== 'bg' && c.op !== 'clear') applyOp(c, i);
      }
    }

    // 선분 하나에 쓸 시간(ms). speed(0)=최고 속도. 그림이 작으면 과정이
    // 보이게 조금 늦추고, 아무리 느린 speed라도 전체 15초는 넘기지 않는다.
    var segTotal = 0;
    cmds.forEach(function (c) { if (c.op === 'seg') segTotal++; });
    var minPace = Math.min(200, 900 / Math.max(segTotal, 1));
    function segCost() {
      var base = speed === 0 ? 0.4 : 260 / speed;
      base = Math.min(base, 15000 / Math.max(segTotal, 1));
      return Math.max(base, minPace);
    }

    var idx = 0, pending = 0, last = 0, cur = null;
    paintBg();
    turtleAnim = { raf: 0 };
    function frame(now) {
      if (!last) last = now;
      pending += Math.min(now - last, 100);
      last = now;
      var guard = 20000;
      while (idx < cmds.length && guard--) {
        var c = cmds[idx];
        if (c.op === 'seg') {
          if (pending < segCost()) break;
          pending -= segCost();
          drawSeg(c);
          var dx = c.x2 - c.x1, dy = c.y2 - c.y1;
          cur = {
            x: c.x2, y: c.y2, v: c.v, c: c.c,
            h: (dx || dy) ? Math.atan2(dy, dx) * 180 / Math.PI
                          : (cur ? cur.h : 0)
          };
        } else {
          applyOp(c, idx);
        }
        idx++;
      }
      octx.clearRect(0, 0, W, H);
      if (idx < cmds.length) {
        if (cur && cur.v) drawShape(octx, cur.x, cur.y, cur.h, cur.c);
        turtleAnim.raf = requestAnimationFrame(frame);
      } else {
        cursors.forEach(function (c) { drawShape(octx, c.x, c.y, c.h, c.c); });
        turtleAnim = null;
      }
    }
    turtleAnim.raf = requestAnimationFrame(frame);
  }

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
      } else if (t === 'turtle') {
        renderTurtle(m);
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
    stopTurtle();
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
    stopTurtle();
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

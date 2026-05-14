/* Pheeew · public site · shared client JS */
(function(){
  'use strict';

  /* PASSCODE GATE
     Single shared password during pre-launch.
     Once entered, sessionStorage keeps it for the rest of the visit
     and the gate is skipped on subsequent reloads.
  */
  var PASSCODE = 'pheeew-2026';
  var GATE_KEY = 'pheeew-site-gate';

  function showGate(){
    var gate = document.getElementById('siteGate');
    if(!gate) return;
    gate.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    var input = document.getElementById('siteGateInput');
    if(input){ setTimeout(function(){ input.focus(); }, 80); }
  }
  function hideGate(){
    var gate = document.getElementById('siteGate');
    if(gate) gate.style.display = 'none';
    document.body.style.overflow = '';
  }
  function checkGate(e){
    if(e) e.preventDefault();
    var input = document.getElementById('siteGateInput');
    var err = document.getElementById('siteGateError');
    if(!input) return false;
    if((input.value || '').trim().toLowerCase() === PASSCODE){
      try{ sessionStorage.setItem(GATE_KEY, '1'); }catch(_){}
      hideGate();
      return false;
    }
    if(err) err.style.display = 'block';
    input.value = '';
    input.focus();
    return false;
  }
  function initGate(){
    var passed = false;
    try{ passed = sessionStorage.getItem(GATE_KEY) === '1'; }catch(_){}
    if(passed){ hideGate(); return; }
    showGate();
    var form = document.getElementById('siteGateForm');
    if(form){ form.addEventListener('submit', checkGate); }
  }

  /* MOBILE NAV TOGGLE */
  function initMobileNav(){
    var toggle = document.querySelector('.nav-mobile-toggle');
    var links = document.querySelector('.nav-links');
    if(!toggle || !links) return;
    toggle.addEventListener('click', function(){
      links.classList.toggle('open');
    });
  }

  /* WAITLIST (no-backend stub)
     Captures the email locally + shows a friendly thanks message.
     Wire to Klaviyo or Shopify when ready by replacing the body of this fn.
  */
  function initWaitlist(){
    document.querySelectorAll('form[data-waitlist]').forEach(function(form){
      form.addEventListener('submit', function(e){
        e.preventDefault();
        var input = form.querySelector('input[type="email"]');
        var btn = form.querySelector('button');
        var note = form.parentElement.querySelector('.waitlist-note');
        if(!input || !input.value) return;
        btn.disabled = true;
        btn.textContent = 'On the list ✓';
        if(note){ note.textContent = "You're in. We'll be in touch when Mojave Sunrise ships."; }
        try {
          var list = JSON.parse(localStorage.getItem('pheeew-waitlist') || '[]');
          list.push({ email: input.value, ts: new Date().toISOString() });
          localStorage.setItem('pheeew-waitlist', JSON.stringify(list));
        } catch(_){}
        input.value = '';
      });
    });
  }

  /* INIT */
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', function(){
      initGate(); initMobileNav(); initWaitlist();
    });
  } else {
    initGate(); initMobileNav(); initWaitlist();
  }
})();

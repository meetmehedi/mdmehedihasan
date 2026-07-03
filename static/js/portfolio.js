// ── Scroll Progress ──
const progressBar = document.getElementById('progress-bar');
function updateProgress() {
  const st = window.scrollY;
  const dh = document.documentElement.scrollHeight - window.innerHeight;
  progressBar.style.width = (dh > 0 ? (st / dh) * 100 : 0) + '%';
}

// ── Nav visibility ──
const nav = document.getElementById('nav');
const navLinks = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('section[id]');
let lastScrollY = 0;
let navVisible = false;

function updateNav() {
  const sy = window.scrollY;
  if (sy > 120 && !navVisible) { nav.classList.add('visible'); navVisible = true; }
  else if (sy <= 120 && navVisible) { nav.classList.remove('visible'); navVisible = false; }
  if (sy > lastScrollY + 5 && sy > 300) { nav.classList.add('hide'); }
  else if (sy < lastScrollY - 5) { nav.classList.remove('hide'); }
  lastScrollY = sy;

  // Active section
  let current = '';
  sections.forEach(s => {
    const top = s.getBoundingClientRect().top;
    if (top < 200) current = s.id;
  });
  navLinks.forEach(l => {
    l.classList.toggle('active', l.getAttribute('href') === '#' + current);
  });
}

// ── Back to top ──
const backTop = document.getElementById('back-top');
function updateBackTop() {
  backTop.classList.toggle('visible', window.scrollY > 600);
}

window.addEventListener('scroll', () => {
  updateProgress();
  updateNav();
  updateBackTop();
}, { passive: true });

// ── Magnetic Cursor ──
const dot = document.getElementById('cursor-dot');
const ring = document.getElementById('cursor-ring');
let mx = -200, my = -200;
let rx = -200, ry = -200;

if (window.innerWidth > 768) {
  window.addEventListener('mousemove', e => {
    mx = e.clientX; my = e.clientY;
    dot.style.left = mx + 'px';
    dot.style.top = my + 'px';
  });
  function animCursor() {
    rx += (mx - rx) * 0.12;
    ry += (my - ry) * 0.12;
    ring.style.left = rx + 'px';
    ring.style.top = ry + 'px';
    requestAnimationFrame(animCursor);
  }
  animCursor();

  document.querySelectorAll('a, button, .bento-cell, .pub-cite-btn, .pub-tab').forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-active'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-active'));
  });
}

// ── Particle System ──
const canvas = document.getElementById('particle-canvas');
const ctx = canvas.getContext('2d');
let W = canvas.width = window.innerWidth;
let H = canvas.height = window.innerHeight;

const PARTICLE_COUNT = Math.min(90, Math.floor(W * H / 14000));
const particles = Array.from({ length: PARTICLE_COUNT }, () => ({
  x: Math.random() * W,
  y: Math.random() * H,
  r: Math.random() * 1.2 + 0.3,
  vx: (Math.random() - 0.5) * 0.18,
  vy: (Math.random() - 0.5) * 0.18,
  a: Math.random(),
  da: (Math.random() - 0.5) * 0.003
}));

function drawParticles() {
  ctx.clearRect(0, 0, W, H);
  particles.forEach(p => {
    p.x += p.vx; p.y += p.vy;
    p.a = Math.max(0.05, Math.min(0.85, p.a + p.da));
    if (p.a <= 0.05 || p.a >= 0.85) p.da *= -1;
    if (p.x < 0) p.x = W; if (p.x > W) p.x = 0;
    if (p.y < 0) p.y = H; if (p.y > H) p.y = 0;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255,255,255,${p.a})`;
    ctx.fill();
  });
  // Draw subtle connecting lines between close particles
  for (let i = 0; i < particles.length; i++) {
    for (let j = i + 1; j < particles.length; j++) {
      const dx = particles[i].x - particles[j].x;
      const dy = particles[i].y - particles[j].y;
      const d = Math.sqrt(dx * dx + dy * dy);
      if (d < 100) {
        ctx.beginPath();
        ctx.moveTo(particles[i].x, particles[i].y);
        ctx.lineTo(particles[j].x, particles[j].y);
        ctx.strokeStyle = `rgba(99,102,241,${(1 - d / 100) * 0.06})`;
        ctx.lineWidth = 0.5;
        ctx.stroke();
      }
    }
  }
  requestAnimationFrame(drawParticles);
}
drawParticles();

window.addEventListener('resize', () => {
  W = canvas.width = window.innerWidth;
  H = canvas.height = window.innerHeight;
});

// ── Scroll Reveal ──
const revealEls = document.querySelectorAll('.reveal');
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); } });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
revealEls.forEach(el => revealObs.observe(el));

// ── Count-up animation ──
function countUp(el) {
  const target = parseFloat(el.dataset.count);
  const decimal = el.dataset.decimal !== undefined;
  const dur = 1200;
  const start = performance.now();
  function frame(now) {
    const p = Math.min((now - start) / dur, 1);
    const v = target * p;
    el.textContent = decimal ? v.toFixed(2) : Math.round(v) + '+';
    if (p < 1) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}
const impactObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting && e.target.dataset.count) {
      countUp(e.target);
      impactObs.unobserve(e.target);
    }
  });
}, { threshold: 0.5 });
document.querySelectorAll('[data-count]').forEach(el => impactObs.observe(el));

// ── Publication Tabs ──
const tabs = document.querySelectorAll('.pub-tab');
const lists = document.querySelectorAll('.pub-list');
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    lists.forEach(l => l.classList.remove('active'));
    tab.classList.add('active');
    const listId = tab.id.replace('tab-', 'list-');
    document.getElementById(listId).classList.add('active');
  });
});

// ── BibTeX Copy ──
// bibEntries is injected inline by Django template (above this script)
function copyBib(key) {
  const bib = bibEntries[key];
  if (!bib) return;
  navigator.clipboard.writeText(bib).then(() => showToast('✓ BibTeX copied to clipboard'));
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2800);
}

// ── Mobile menu ──
const menuToggle = document.getElementById('menuToggle');
const desktopLinks = document.querySelector('.desktop-links');
menuToggle.addEventListener('click', () => {
  const open = desktopLinks.style.display === 'flex';
  desktopLinks.style.display = open ? 'none' : 'flex';
  desktopLinks.style.flexDirection = 'column';
  desktopLinks.style.gap = '4px';
  desktopLinks.style.padding = '8px 0';
});
document.querySelectorAll('.nav-link').forEach(l => {
  l.addEventListener('click', () => {
    if (window.innerWidth <= 768) desktopLinks.style.display = 'none';
  });
});

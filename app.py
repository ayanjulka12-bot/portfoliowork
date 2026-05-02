<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{{ project.name }} - Portfolio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2 family=Sora:wght@300;400;600;700;800&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="/static/styles.css" />
</head>
<body>

<nav class="nav-bar">
  <a href="/" class="nav-logo">dev<span>.</span></a>
  <a href="/#lab" class="btn-magnetic" style="font-size:0.78rem; padding:0.6rem 1.4rem;"><- Back to Lab</a>
</nav>

<section style="min-height:100vh; padding: 8rem 2.5rem 4rem; max-width:900px; margin:0 auto;">

  <p class="section-label">// {{ project.status }}</p>

  <h1 class="font-head font-extrabold mb-4" style="font-size: clamp(2rem,5vw,3.8rem); letter-spacing:-0.03em; line-height:1.1;">
    {{ project.name }}
  </h1>

  <p class="text-cyan font-mono text-sm mb-8">{{ project.tagline }}</p>

  <div class="glass p-8 mb-8" style="border-color: rgba(6,182,212,0.2);">
    <p class="text-zinc-300 leading-relaxed">{{ project.description }}</p>
  </div>

  {% if project.stack %}
  <div class="mb-8">
    <p class="section-label mb-4">// Stack</p>
    <div class="flex flex-wrap gap-3">
      {% for tech in project.stack %}
      <span class="font-mono text-xs px-3 py-1 rounded-full" style="background: rgba(6,182,212,0.08); border: 1px solid rgba(6,182,212,0.25); color: #06b6d4;">{{ tech }}</span>
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if project.metrics %}
  <div class="mb-8">
    <p class="section-label mb-4">// Build Log</p>
    <div class="timeline">
      {% for m in project.metrics %}
      <div class="timeline-item" style="opacity:1; transform:none;">
        <div class="event">{{ m }}</div>
      </div>
      {% endfor %}
    </div>
  </div>
  {% endif %}

  <a href="/#connect" class="btn-magnetic">Work Together -></a>

</section>

<footer>
  <span>Built from scratch. Shipped in weeks. &nbsp;.&nbsp; &copy; 2026</span>
</footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script>
  gsap.from('h1, .section-label, .glass, .btn-magnetic', {
    opacity: 0, y: 25, duration: 0.8, stagger: 0.1, ease: 'expo.out', delay: 0.1,
  });
</script>
</body>
</html>

// Placeholder for future interactivity
document.addEventListener('DOMContentLoaded', () => {
  // Smooth scroll for same-page anchors
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href').slice(1)
      const el = document.getElementById(id)
      if (el) {
        e.preventDefault()
        el.scrollIntoView({ behavior: 'smooth' })
      }
    })
  })

  // Theme toggle (light/dark) with localStorage
  const html = document.documentElement
  const btn = document.querySelector('[data-theme-toggle]')
  const iconDark = document.querySelector('[data-icon-dark]')
  const iconLight = document.querySelector('[data-icon-light]')
  function setTheme(theme) {
    html.setAttribute('data-theme', theme)
    html.setAttribute('data-bs-theme', theme)
    const meta = document.querySelector('meta[name="theme-color"]')
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#0b0f17' : '#f7f9ff')
    if (iconDark && iconLight) {
      if (theme === 'dark') { iconDark.classList.remove('d-none'); iconLight.classList.add('d-none') }
      else { iconDark.classList.add('d-none'); iconLight.classList.remove('d-none') }
    }
  }
  if (btn) {
    btn.addEventListener('click', () => {
      const current = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'
      localStorage.setItem('theme', current)
      setTheme(current)
    })
    setTheme(html.getAttribute('data-theme') || 'dark')
  }
})


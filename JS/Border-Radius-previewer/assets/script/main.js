let radiusBorder = document.querySelector('.bdr-rds')
radiusBorder.addEventListener('keypress', e => {
  console.log('executando sistema')
  const border1 = document.querySelector('radio-1')
  const border2 = document.querySelector('radio-2')
  const border3 = document.querySelector('radio-3')
  const border4 = document.querySelector('radio-4')
  let el = e.target
  console.log(el)
  if (el.classList.contains('radio-1')) {
    radiusBorder.style.borderRadius = `${border1} 0px 0px 0px`
  }
  if (el.classList.contains('radio-2')) {
    radiusBorder.style.borderRadius = `0px ${border2} 0px 0px`
  }
  if (el.classList.contains('radio-3')) {
    radiusBorder.style.borderRadius = ` 0px 0px ${border3} 0px`
  }
  if (el.classList.contains('radio-4')) {
    radiusBorder.style.borderRadius = `0px 0px 0px ${border4}`
  }

  console.log('fim da execução')
})

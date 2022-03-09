function radiusBorder() {
  console.log('executando sistema')
  let border1 = document.querySelector('#radio1').value
  let border2 = document.querySelector('#radio2').value
  let border3 = document.querySelector('#radio3').value
  let border4 = document.querySelector('#radio4').value
  let borderValue = document.querySelector('.create-border')

  let borderStyle = document.querySelector('.create-border').style

  borderStyle.borderTopLeftRadius = `${border1}%`

  borderStyle.borderTopRightRadius = `${border2}%`

  borderStyle.borderBottomLeftRadius = `${border3}%`

  borderStyle.borderBottomRightRadius = `${border4}%`

  borderValue.innerHTML = `<p>${border1}% ${border2}% ${border3}% ${border4}%</p>`
  console.log('fim da execução')
}

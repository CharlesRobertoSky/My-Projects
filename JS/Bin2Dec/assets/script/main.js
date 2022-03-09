function conversor() {
  const converter = document.querySelector('#converter')
  converter.addEventListener('click', e => {
    const valor = document.querySelector('#busca')
    let res = document.querySelector('.res')
    var v = Number(valor.value)
    if (v == 0) {
      console.log('por favor digite um número válido')
      res.innerHTML = '<p>Por favor digite um número válido</p>'
    } else {
      console.log('tudo certo, executando função')
      var binario = v.toString(2)
      console.log(binario)
      res.innerHTML = `<p>Seu número em binário: ${binario}</p>`
    }
    console.log(v)
  })
}
conversor()

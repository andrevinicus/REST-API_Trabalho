
#2 - API de aluguel de carros

A locadora XPTO possui 10 carros de mesma marca, modelo, ano e cor e precisa de uma forma de controlar a locação dos carros. Para isso, ela precisa de uma API REST onde pode cadastrar uma nova locação com nome do cliente e data de saída do veículo. Deve listar todas as locações que estão em aberto. Deve permitir atualizar a locação com a data de finalização.Também deve permitir a exclusão de uma locação em aberto. Os dados devem ser gravados em memória e vão existir enquanto a aplicação existir.

```json
{
    "nome_cliente": "Fulano de tal",
    "placa_veiculo": "ABC1A12",
}
```

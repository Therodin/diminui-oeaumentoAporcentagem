i = str(input('Deseja caucular um aumento ou um abaixo salarial?: '))


if i == 'aumento':
    am = float(input('Qual o salário do funcionario? R$: '))
    pc = float(input('Qual a porcentagem do reajuste?: '))

    ea = am + (am * pc / 100)
    print(f'O aumento em {pc:.0f}% salarial do funcionario ficará {ea:.2f}' )

else:
      i = 'abaixo'
      ab = float(input('Qual a porcentagem do reajuste?: '))
      pct = float(input('Qual a porcentagem do reajuste?: '))

      ae = ab - (ab * pct / 100)
      print(f'O desconto salarial avaliado em {pct:.0f}% do funcionário será {ae:.2f}')
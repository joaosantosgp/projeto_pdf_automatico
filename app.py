from fpdf import FPDF 

projeto = input('Digite a descrição do projeto: ')
horas_previstas = int(input('Digite a quantidade de horas previstas: '))
valor_hora = int(input('Digite o valor da hora trabalhada (R$): '))

valor_projeto = horas_previstas * valor_hora

pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial', style='B')
pdf.image("template.png", x=0, y=0)

pdf.text(115, 198, projeto)
pdf.text(115, 217, str(horas_previstas))
pdf.text(115, 233, str(valor_hora))
pdf.text(115, 250, str(valor_projeto))


pdf.output('Orçamento.pdf')
print("\033[1;32mOrçamento gerado com sucesso!\033[0m")
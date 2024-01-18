from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_summary(results):
    filename = "load_test_summary.pdf"

    with canvas.Canvas(filename, pagesize=letter) as pdf:
        pdf.drawString(100, 800, "Resumo do Teste de Carga")
        pdf.drawString(100, 780, "---------------------------------")

        # Adicione informações resumidas para cada resultado individual
        y_position = 760
        for result in results:
            pdf.drawString(100, y_position, f"Usuário {result['user_id']}")
            pdf.drawString(120, y_position - 20, f"Status da Resposta: {result['response_status']}")
            pdf.drawString(120, y_position - 40, f"Tempo de Resposta: {result['elapsed_time']:.2f} segundos")
            pdf.drawString(100, y_position - 60, "---------------------------------")
            y_position -= 80

        # Adicione informações gerais
        pdf.drawString(100, y_position, "Informações Gerais:")
        pdf.drawString(120, y_position - 20, f"Total de Usuários: {len(results)}")
        # Adicione outras informações gerais que desejar

    print(f"Relatório geral gerado: {filename}")

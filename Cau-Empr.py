from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class LoanApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        self.valor_input = TextInput(hint_text='Valor da Casa (R$)', input_filter='float')
        self.salario_input = TextInput(hint_text='Salário Mensal (R$)', input_filter='float')
        self.prazo_input = TextInput(hint_text='Prazo do Empréstimo (anos)', input_filter='int')

        layout.add_widget(Label(text='Valor da Casa (R$):'))
        layout.add_widget(self.valor_input)

        layout.add_widget(Label(text='Salário Mensal (R$):'))
        layout.add_widget(self.salario_input)

        layout.add_widget(Label(text='Prazo do Empréstimo (anos):'))
        layout.add_widget(self.prazo_input)

        calcular_button = Button(text='Calcular', on_press=self.calcular_emprestimo)
        layout.add_widget(calcular_button)

        return layout

    def calcular_emprestimo(self, instance):
        try:
            valor_casa = float(self.valor_input.text)
            salario_comprador = float(self.salario_input.text)
            prazo_emprestimo = int(self.prazo_input.text)
        except ValueError:
            self.mostrar_erro("Por favor, preencha todos os campos com valores numéricos.")
            return

        if prazo_emprestimo <= 0:
            self.mostrar_erro("O prazo do empréstimo deve ser maior que zero.")
            return

        prazo_meses = prazo_emprestimo * 12
        taxa_juros_anual = 0.1  # Taxa de juros anual (exemplo)

        prestacao_mensal = (valor_casa * (1 + taxa_juros_anual)**(1 / 12)) / (1 - (1 + taxa_juros_anual)**(-prazo_meses))

        if prestacao_mensal <= 0.3 * salario_comprador:
            self.mostrar_mensagem("Empréstimo Aprovado! Prestação Mensal: R$ {:.2f}".format(prestacao_mensal))
        else:
            self.mostrar_mensagem("Empréstimo Negado! A prestação excede 30% do salário.")

    def mostrar_mensagem(self, mensagem):
        popup = Popup(title='Resultado', content=Label(text=mensagem), size_hint=(None, None), size=(400, 200))
        popup.open()

    def mostrar_erro(self, mensagem):
        popup = Popup(title='Erro', content=Label(text=mensagem), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    LoanApp().run()

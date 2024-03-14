# Importando as bibliotecas necessárias
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import math

class LoanApp(App):
    def build(self):
        # Layout da interface
        layout = GridLayout(cols=2)

        # Labels e Inputs para os dados
        layout.add_widget(Label(text='Valor da Casa (R$):'))
        self.valor_input = TextInput(input_filter='float')
        layout.add_widget(self.valor_input)

        layout.add_widget(Label(text='Salário Mensal (R$):'))
        self.salario_input = TextInput(input_filter='float')
        layout.add_widget(self.salario_input)

        layout.add_widget(Label(text='Prazo do Empréstimo (anos):'))
        self.prazo_input = TextInput(input_filter='int')
        layout.add_widget(self.prazo_input)

        # Botão para calcular
        calcular_button = Button(text='Calcular')
        calcular_button.bind(on_press=self.calcular_emprestimo)
        layout.add_widget(calcular_button)

        return layout

    def calcular_emprestimo(self, instance):
        # Obtendo os dados inseridos pelo usuário
        try:
            valor_casa = float(self.valor_input.text)
            salario_comprador = float(self.salario_input.text)
            prazo_emprestimo = int(self.prazo_input.text)
        except ValueError:
            self.mostrar_erro("Por favor, preencha todos os campos com valores numéricos.")
            return

        # Calculando a prestação mensal
        prestacao_calculada = self.calcular_prestacao_mensal(valor_casa, salario_comprador, prazo_emprestimo)

        # Verificando a condição de aprovação do empréstimo
        if prestacao_calculada <= 0.3 * salario_comprador:
            self.mostrar_mensagem("Empréstimo Aprovado! Prestação Mensal: R$ {:.2f}".format(prestacao_calculada))
        else:
            self.mostrar_mensagem("Empréstimo Negado! A prestação excede 30% do salário.")

    def calcular_prestacao_mensal(self, valor_casa, salario_comprador, prazo_emprestimo):
        # Convertendo o prazo do empréstimo de anos para meses
        prazo_meses = prazo_emprestimo * 12

        # Solicitando a taxa de juros anual ao usuário
        taxa_juros_anual = float(input("Digite a taxa de juros anual (%): "))
        
        # Calculando a taxa de juros mensal com base na taxa anual
        taxa_juros_mensal = (1 + (taxa_juros_anual / 100))**(1 / 12) - 1
        
        # Calculando a prestação mensal usando a fórmula de amortização
        prestacao_mensal = (valor_casa * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal)**-prazo_meses)
        
        return prestacao_mensal

    def mostrar_mensagem(self, mensagem):
        popup = Popup(title='Resultado', content=Label(text=mensagem), size_hint=(None, None), size=(400, 200))
        popup.open()

    def mostrar_erro(self, mensagem):
        popup = Popup(title='Erro', content=Label(text=mensagem), size_hint=(None, None), size=(400, 200))
        popup.open()

# Executando o aplicativo
if __name__ == '__main__':
    LoanApp().run()

from prettytable import PrettyTable
"""Module that help format table very well in ASCII"""
table = PrettyTable()
table.add_column("Pokemon", ['pickachu', 'squirtle', 'combee'])
table.add_column("Type", ['electric', 'water', 'fire'])
table.align = 'l'
print(table)

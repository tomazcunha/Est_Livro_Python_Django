


# --------------------------------
#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# --------------------------------
# Importando módulos
    import random
    numero = random.randint(1, 100)


# --------------------------------
# Entrada de dados
    escolha = input("Escolha um número entre 1 e 100    :")


# --------------------------------
# Loop while
    while escolha != numero:


# --------------------------------
# Condicional If
    if escolha < numero:
            print "O número", escolha, "é nemor que o sorteado."
        elif escolha > numero:
            print "O número", escolha, "é maior que o sorteado."

# --------------------------------
# Parêmetros de variáveis de ambiente

    pythom -h # motra todos os parâmetros
    -h, -O, -OO, -i, -c cmds, -t, -u, -E, -S, -v, -x, -m módulo, -W parm (ignore, default, all, module, once, error)

# Variáveis de ambiente

    PYTHONHOME # define o diretório em que o python foi instalado
    PYTHONPATH # define a ordem de procura de diretórios usados para importar os módulos python
    PYTHONSTARTUP
    PYTHONOPTIMIZE
    PYTHONDEBUG
    PYTHONINSPECT
    PYTHONUNBUFFERED
    PYTHONVERBOSE

# Exportando um módulo que abilita o autocompletar de comando no interprtador python
    ~/.bashrc
        export PYTHONSTARTUP="$HOME/.pystartup"

            import atexit
            import os
            import readline
            import rlcompleter

            readline.parse_and_bind("tab: complete")
            historyPath = os.path.expanduser("~/.pyhistory")

            def save_history(historyPath=historyPath):
                import readline
                readline.write_history_file(historyPath)

            if os.path.exists(historyPath):
                readline.read_history_file(historyPath)

            atexit.register(save_history)
            del os atexit, readline, rlcompleter, save_history, historyPath

from xmlbuilder import element

if __name__ == "__main__":
    b = element("eSocial")
    t = element("trabalhador")
    t.value("trab")
    b.evtTrabalhador(t).build()

    print(b)

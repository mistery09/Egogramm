
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *



questions = [
("Bei einer Fahrausweiskontrolle mit einem ungültigen Fahrausweis erwischt zu werden wäre mit höchst unangenehm", "aK"), #1.
("An 'das was man tut oder nicht', fühle ich mich kaum gebunden", "fK"), #2.
("Sage mir, mit wem du befreundet bist und ich sage dir, wer du bist", "kEL"), #3.
("Ich habe ungern mit Verwaltungsstellen zu tun, weil ich mich dann meist hilflos fühle", "aK"), #4.
("Ich bin oft verspielt und lustig", "fK"), #5.
("Menschen im Alltag zu unterstützen Ihren eigenen Weg zu finden ist für mich eine ineere Befriedigung", "fEL"), #6.
("Leute die dauernd darüber klagen, wie schlecht es ihnen geht, kann ich nicht verstehen.", "ER"), #7.
("Ordnung ist das halbe Leben", "kEL"), #8.
("Die Welt ist heute auch nicht mehr, was sie mal war.", "kEL"), #9.
("Mir einen Fehler einzugestehen und das auch noch zuzugeben fällt mir schwer", "rK"), #10.
("Es ist wunderbar, dass wir trotz vieler misslicher Umständee im Leben immer wieder die schönen Dinge des Lebens sehen können", "fK"), #11.
("Wenn die nächste Diskussion wieder so ziellos verläuft, dann haue ich aber mit der Faust auf den Tisch", "rK"), #12.
("Ich strenge mich an, damit ich die Erwartungen der anderen erfülle", "aK"), #13.
("Andere bitten mich oft um Rat in schwierigen Situationen", "fEL"), #14.
("Man sollte mehr Rücksicht aufeinander nehemen", "kEL"), #15.
("In fremden Städten finde ich mich leicht zurecht", "ER"), #16.
("Spontan und intuiti ist eine meiner Stärken", "fK"), #17.
("Es ist wichtig mehr Rücksicht aufeinander zu nehmen", "fEL"), #18.
("'Liebe Deinen Nächsten wie Dich selbst' - hat heute wie früher immer noch seine Berechtigung", "fEL"), #19.
("Wenn ich etwas einkaufe, fällt es mir schwer etwas nicht zu kaufen, wenn sich die Verkäuferin sehr viel Mühe mit mir gegeben hat.", "aK"), #20.
("Kinder brauchen viel Geborgenheit und Zuwendung, das Leben ist noch hart genug später", "fEL"), #21.
("Entscheidungen treffe ich gerne selbst und überlege mir gründlich das Pro und Contra", "ER"), #22.
("Manchmal bin ich wie ein kleines Kind.", "fK"), #23.
("Wenn ich die Meinung anderer nicht teile, so versuche ich doch, diese zu verstehen", "ER"), #24.
("'Solange du deine Füße unter mein Tisch streckst, hast Du zu tun, was ich sage'", "kEL"), #25.
("Wenn ich etwas nicht verstanden habe, frage ich nach, bis es mir klar ist.", "ER"), #26.
("Regeln sind einzuhalten", "kEL"), #27.
("Meine Kollegen zu unterstützen ist eine Selbstverständlichkeit für mich", "fEL"), #28.
("Wenn ich aufgefordert werde etwas zu tun, mache ich am liebsten das Gegenteil davon.", "rK"), #29.
("Gegenüber anderen bin ich eher versöhnlich und nachsichtig", "fEL"), #30.
("Schon gar nicht würde ich in einer schwierigen Situation nachgeben", "rK"), #31.
("Manchmal habe ich heute immer noch Lust so wie als Kind früher Klingelstreiche an Mietshäusern zu spielen", "fK"), #32.
("Lügen haben kurze Beine", "kEL"), #33
("Diese Arbeit würde ich nur an jemanden vergeben, der weiß, wie er sich zu benehmen hat.", "kEL"), #34.
("Soziale Einrichtungen unterstütze ich so gut ich kann", "fEL"), #35.
("Ich zeige anderen, wenn ich sie mag", "fK"), #36.
("Wie komme ich dazu auf andere Rücksicht zu nehmen", "rK"), #37.
("Meine Freude offen zu zeigen fällt mir immer wieder leicht", "fK"), #38.
("Meine Meinung zu ändern fällt mir leicht, wenn ich das Problem einsehe", "ER"), #39.
("Die Fassung verliere ich nicht schnelle", "ER"), #40.
("Eher stimme ich anderen zu, als dass ich klar und deutlich meine Meinung vertrete", "aK"), #41.
("Wenn mir was gefällt, will ich es unbedingt haben.", "fK"), #42
("Ich habe  den Ruf, objektiv zu sein", "ER"), #43
("Ich ture oft etwas dafür, damit mich die anderen akzeptieren", "aK"), #44
("Meist weiß ich was ich sage, aber nicht immer, was ich denke", "ER"), #45
("Lachen ist die beste Medizing", "fK"), #46
("Manchmal möchte ich am liebsten alles hinschmeißen und abhauen", "rK"), #47
("Ich gehe ungern alleine neue Schritte im Leben.", "aK"), #48
("Weiterbildung ist für mich total wichtig", "ER"), #49
("Ich denke schon mal 'denen werde ichs zeigen'", "rK"), #50
("Für die Hilfebedürftigen in der Dritten Welt ist es totatl wichtig, dass wir hier Projekte starten", "fEL"), #51
("Ich versuche gern meinen Kopf durchzusetzen", "rK"), #52.
("Gerne sorge ich für andere", "fEL"), #53.
("Arbeit hat noch keinem geschadet", "kEL"), #54
("Bei Rot würde ich im Leben nicht über die Straße gehen", "aK"), #55.
("Es fällt mir schwer Autorität von anderen zu aktzeptieren", "rK"), #56.
("Was ich auch tue, es muss so perfekt wie möglich sein", "aK"), #57.
("Die die keine Arbeit haben, tun zu wenig dafür", "kEL"), #58.
("Wenn ich mich unwohl fühle ziehe ich mich gern zurück", "aK"), #59.
("Und schon gar nicht lass ich mir etwas befehlen", "rK") #60.
]  







def show():
    vars_result = list(map(lambda x: x.get(), vars))

    points =  {"kEL": 0, "fEL": 0, "ER": 0, "fK": 0, "rK": 0, "aK": 0}

    for result, question in zip(vars_result, questions):
        if result == 1:
            points[question[1]] += 1

    
    print(points)


    fig = plt.figure()
    ax = plt.axes()

    ax.bar(points.keys(), points.values())
    plt.show()






root = Tk()
root.geometry("400x700")



main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

vars = []

for index, question in enumerate(questions):
    var = IntVar()
    vars.append(var)
    Checkbutton(second_frame, text=f'{index+1}. {question[0]}', variable=var).pack()



button = Button(second_frame, text="submit", command=show)
button.pack()


root.mainloop()


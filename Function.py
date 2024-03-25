import tkinter
import tkinter.filedialog
scep = 0


def save_file(variab, labes):

    if scep == 7:
        quest_chep = 0

        score_file = tkinter.filedialog.asksaveasfilename(filetypes=[("Текстові файли", "*.txt"), ("Усі файли", "*.*")])

        try:
            if score_file != "":
                with open(score_file + ".txt", "w", encoding="utf-8") as score_file:
                    for i in variab.quest_correct:
                        score_file.write(f"Питання {labes[quest_chep]['text']} - {i.get()}" + "\n")
                        quest_chep += 1
                    score_file.write(f"Результат - {variab.score}/7")
        except:
            pass


def show_score(variab, labes):


    if scep == 7:
        quest_chep = 0

        score_disp = tkinter.Tk()
        score_disp.geometry("300x400")
        lab = [tkinter.Label(score_disp),
               tkinter.Label(score_disp),
               tkinter.Label(score_disp),
               tkinter.Label(score_disp),
               tkinter.Label(score_disp),
               tkinter.Label(score_disp),
               tkinter.Label(score_disp)]
        for i in variab.quest_correct:
            lab[quest_chep].config(text=f"Питання {labes[quest_chep]['text']} - {i.get()}")
            lab[quest_chep].pack()
            quest_chep += 1

        tkinter.Label(score_disp, text=f"Результат - {variab.score}/7").pack()




def score_defer(variab):
    for i in variab.quest_correct:
        if i.get() == "Correct":
            variab.score += 1



def start_test(variab, r_bs, butts, labels):
    global scep
    if scep != 7:
        ind = 0
        chor = 0

        text = labels.quest_label[scep]
        labels.mask_l.config(text=text['text'])
        labels.mask_l.place(relx=0.4, rely=0.1)
        butts.place(relx=0.4, rely=0.8)
        for i in r_bs.mask:
            quest = r_bs.quest[scep][ind]
            i.config(text=quest['text'], variable=quest['variable'], value=quest['value'])
            i.place(relx=0.4, rely=0.2 + chor)
            ind += 1
            chor += 0.1


        scep += 1
    else:
        score_defer(variab)
        print(variab.score)
        butts.config(state="disabled")


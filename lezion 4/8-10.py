def show_message(mylist) ->list[str]:
    for item in mylist:
        print("\n",item)


def send_message(original_list, sent_messages) ->list[str]:
    for item in original_list:
        sent_messages.append(item)
        if original_list.pop(0):
            show_message(sent_messages)
            show_message(original_list)

original_list:list[str]=["ciao sto male","domani sto in ferie","nessuno sta bene","perche stai in ritardo"]
sent_messages:list[str]=[]

send_message(original_list, sent_messages)
    






        



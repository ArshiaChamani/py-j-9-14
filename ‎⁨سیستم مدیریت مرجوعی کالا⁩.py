





#سیستم مدیریت مرجوعی کالا

list_kala_anbar= []
list_shomer_faktor= []
list_marjoei= []
list_vajh_bazgashti=[]
sharayet_marjooei= ["1-naghs_kala   2-shekastegi    3-moghayerat_dar_sefaresh     4-sayer"]
list_elat_marjooei=[]
zayeat=[]

while True:
    menu= input ("1-sabt_kala_ha      2-sabt_shomare_faktor     3-entekhab_kala_marjooei      4-namayesh_marjooei      5-exit: ")
    while True:
        match menu:
            case "1":
                products= input ("mahsoolat ra vared konid: ").casefold()
                list_kala_anbar.append(products)
                print ("kala ha sabt shod: ", 
                       list_kala_anbar)
                break
            case "2":
                faktor= input ("shomere faktor mahsoolat kharidari shode ra sabt konid: ")
                list_shomer_faktor.append(faktor)
                print ("shomare faktor ha sabt shod: " , 
                       list_shomer_faktor)
                break
            case "3":
                nam_kala_marjooei= input ("nam kala marjooei ra vared konid: ").casefold()
                print (nam_kala_marjooei)
                print (sharayet_marjooei)
                elat_marjooei= int (input ("bar asas sharayet marjooei shomare vared konid: "))
                if elat_marjooei==1:
                    list_elat_marjooei.append("naghs kala")
                    list_marjoei.append(nam_kala_marjooei)
                    zayeat.append(nam_kala_marjooei)
                    print ("elat marjooei pazirofte ast.")
                elif elat_marjooei==2:
                    list_elat_marjooei.append("shekastegi")
                    list_marjoei.append(nam_kala_marjooei)
                    zayeat.append(nam_kala_marjooei)
                    print ("elat marjooei pazirofte ast.")
                elif elat_marjooei==3:
                    list_elat_marjooei.append("moghayerat dar sefaresh.")
                    list_marjoei.append(nam_kala_marjooei)
                    list_kala_anbar.append(nam_kala_marjooei)
                    print ("elat marjooei pazirofte ast.")   
                else:
                    print ("sharayet marjoo ghabel ghabool nist.")
                    break
                print (list_shomer_faktor)
                shomare_faktor_marjooei= int (input ("shomare faktor kala marjooei ra vared konid: "))
                print ("shomare faktor sabt shod: ", shomare_faktor_marjooei)
                from datetime import datetime
                sabt_tarikh_kharid= input ("tarikh kharid ra vared konid (YYYY-MM-DD): ")
                tarikh_kharid= datetime.strptime (sabt_tarikh_kharid, "%Y-%m-%d")
                print ("tarikh kharid: ", tarikh_kharid)
                sabt_tarikh_marjooei= input ("tarikh marjoo ra vared konid (YYYY-MM-DD): ")
                tarikh_marjoo= datetime.strptime (sabt_tarikh_marjooei, "%Y-%m-%d")
                print ("tarikh marjoo: ", tarikh_marjoo)
                ekhtelaf= tarikh_marjoo - tarikh_kharid
                if 0<= ekhtelaf.days <=7:
                    print ("kala ghabel marjoo ast. ")
                else:
                    print ("mohlat marjooei be payan reside ast. ")
                    break
                mablagh_pardakhti= int (input ("mablagh pardakht shode ra vared konid: "))
                print ("pardakhti=", mablagh_pardakhti)
                vajh_bazgashti= mablagh_pardakhti * 0.8
                print ("vajh ghabel bazgasht= ", vajh_bazgashti)
                list_vajh_bazgashti.append(vajh_bazgashti)
                break
            case "4":
                print(list_marjoei)
                break
            case "5":
                print ("elat marjoo: ", list_elat_marjooei)
                print ("nam kala haye marjoo shode: " , list_marjoei)
                print ("tedad kala haye marjoo shode= ", (len(list_marjoei)))
                print ("majmooe vajh bazgashti= ", sum(list_vajh_bazgashti))
                print ("kala haye mojood: ", list_kala_anbar)
                print ("aghlam gheir ghabel estefade" , zayeat)
                print ("Bye\U0001F44B")
                break
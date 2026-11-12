




list_moshakhasat_safir=[]
list_daramad_safar=[]
list_daramad_marsoole=[]
list_kol_daramad=[]

while True:
    menu= input("1-sabt_nam_safir     2-darkhast_safar     3-darkhast_ersal_kala      4-exit: ")
    while True:
        match menu:
            case "1":
                full_name= input ("nam khod ra kamel vared konid: ")
                full_name= full_name.title()
                print ("full name= ", full_name)
                age= int (input ("sen safir?: "))
                if age<18:
                    print (full_name , "mojaz be sabt nam nist")
                    break
                else:
                    print ("sen sabt shod")
                khodro= input ("nam khodro ra vared konid: ")
                print ("Car= ", khodro)
                model_khodro= int (input ("model khodro ra vared konid: "))
                print ("Model= ", model_khodro)
                rang_khodro= input ("rang khodro ra vared konid: ")
                print ("rang= ", rang_khodro)
                pelak_khodro= input ("shomare pelak ra vared konid: ")
                print ("shomare pelak= ", pelak_khodro)
                list_moshakhasat_safir.append(full_name)
                list_moshakhasat_safir.append(khodro)
                list_moshakhasat_safir.append(model_khodro)
                list_moshakhasat_safir.append(rang_khodro)
                list_moshakhasat_safir.append(pelak_khodro)
                print ("moshakhasat: ", list_moshakhasat_safir)
                break

            case "2":
                distance= float (input ("masafat ra metric vared konid: "))
                print ("masafat= ", distance ,"km")
                price_per_km= int (input ("keraye be ezaye har kilometer ra vared konid: "))
                print (price_per_km , "toman")
                mablagh_safar= distance * price_per_km
                print ("pardikhti mosafer= ", mablagh_safar , "toman")

                #مبلغ دریافتی سفیر با کسر 20% کمیسیون محاسبه میشود.
                mablagh_daryafti_safir= mablagh_safar * 0.8
                list_daramad_safar.append(mablagh_daryafti_safir)
                list_kol_daramad.append(mablagh_daryafti_safir)
                print ("daryafti safir az safar=", list_daramad_safar)
                break 

            case "3":
                distance_2= float(input ("masafat ra metric vared konid: "))
                print ("masafat= ", distance_2 ,"km")
                price_2_per_km= int (input ("keraye be ezaye har kilometer ra vared konid: "))
                print (price_2_per_km , "toman")
                hazine_ayab_zahab= distance_2 * price_2_per_km
                print ("ayab zahab= ", hazine_ayab_zahab , "toman")
                weight= float (input ("vazn mahsool ra kg vared konid: "))
                print ("vazn kala=", weight , "kg")
                price_per_kg= int (input ("keraye be ezaye har kg ra vared konid: "))
                print (price_per_kg , "toman")
                hazine_kala= weight * price_per_kg
                print ("hazine kala= " ,hazine_kala , "toman")
                mablagh_pardakhti= hazine_kala + hazine_ayab_zahab
                print ("pardakhti moshtari= " , mablagh_pardakhti , "toman")
                daryafti_safir= (hazine_ayab_zahab * 0.8) + hazine_kala
                list_daramad_marsoole.append(daryafti_safir)
                list_kol_daramad.append(daryafti_safir)
                print ("daryafti safir az ersal kala= ", list_daramad_marsoole)
                break

            case "4":
                print (list_moshakhasat_safir)
                print ("kol daryafti= " , sum(list_kol_daramad))
                break 


                
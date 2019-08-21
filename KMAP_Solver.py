#Name: Isha Gupta
#Roll no: 2018040
#Section: A
#Group: 8
def minterm_binary(numVar,t):
    if t=="0":
        a="0000"
    elif t=="1":
        a="0001"
    elif t=="2":
        a="0010"
    elif t=="3":
        a="0011"
    elif t=="4":
        a="0100"
    elif t=="5":
        a="0101"
    elif t=="6":
        a="0110"
    elif t=="7":
        a="0111"
    elif t=="8":
        a="1000"
    elif t=="9":
        a="1001"
    elif t=="10":
        a="1010"
    elif t=="11":
        a="1011"
    elif t=="12":
        a="1100"
    elif t=="13":
        a="1101"
    elif t=="14":
        a="1110"
    elif t=="15":
        a="1111"
    end=(-1*numVar)-1
    s=""
    for i in range(-1,end,-1):
        s=a[i]+s
    return s
def check_comb(s1,s2):
    count=0
    pos=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
            pos=i
    if count==1:
        s1l=list(s1)
        s1l[pos]="-"
        s1="".join(s1l)
        s2l=list(s2)
        s2l[pos]="-"
        s2="".join(s2l)
        return True,s1,s2
    else:
        return False,s1,s2
def making_pi(flag_list,group_list,pie):
    for i in group_list:
        for j in i:
            x=j
            if type(j)!="<class \'str\'>":
                x=sorted(j)
            if j not in flag_list and x not in pie:
                pie.append(x)
    return pie
def minFunc(numVar,stringIn):
    epi=[]
    t=stringIn.find(")")
    tempp=(stringIn[1:t])
    terms=tempp.split(",")
    t2=(stringIn.find("d"))+1
    dcterms=[]
    l0=[]
    l0_terms=[]
    l1=[]
    l1_terms=[]
    l2=[]
    l2_terms=[]
    l3=[]
    l3_terms=[]
    l4=[]
    l4_terms=[]
    if stringIn[t2+1]!="-":
            temp2=stringIn[t2+2:len(stringIn)-1]
            dcterms=temp2.split(",")
    main_list=terms+dcterms
    
    for i in main_list:
        ans=minterm_binary(numVar,i)
        x=ans.count("1")
        if x==0:
            l0_terms.append(i)
            l0.append(ans)
        elif x==1:
            l1_terms.append(i)
            l1.append(ans)
        elif x==2:
            l2_terms.append(i)
            l2.append(ans)
        elif x==3:
            l3_terms.append(i)
            l3.append(ans)
        elif x==4:
            l4_terms.append(i)
            l4.append(ans)
    pi=[]
    pi_terms=[]
    first_list=[[l0_terms,l0],[l1_terms,l1],[l2_terms,l2],[l3_terms,l3],[l4_terms,l4]]
    
    c=first_list.count([[],[]])
    for i in range(c):
        first_list.remove([[],[]])
    #print (first_list,"first list")
    #print (main_list,"main_list")
    pair_list=[[],[],[],[]]
    pair_terms=[[],[],[],[]]
    flag_pair=[]
    #print (first_list)
    for i in range(len(first_list)-1):
        if first_list[i]!=[[],[]] and first_list[i+1]!=[[],[]]:
            for j in range(len(first_list[i][1])):
                l_temp=first_list[i][1]
                for k in range(len(first_list[i+1][1])):
                    boole,s1,s2=check_comb(l_temp[j],first_list[i+1][1][k])
                    if boole:
                        x1=s1.count("1")
                        #print (x1,"count")
                        pair_list[x1].append(s1)
                        #print (pair_list,x1)
                        pair=[first_list[i][0][j],first_list[i+1][0][k]]
                        #print (pair,"pairs")
                        pair_terms[x1].append(pair)
                        flag_pair.append(first_list[i][0][j])
                        flag_pair.append(first_list[i+1][0][k])
    for i in terms:
        if i not in flag_pair:
            pi.append(minterm_binary(numVar,i))
            pi_terms.append(i)
    c2=pair_list.count([])
    #print (pair_list,"pair list")
    for i in range(c2):
        pair_list.remove([])
        pair_terms.remove([])
        
    quad_terms=[[],[],[]]
    quad_list=[[],[],[]]
    flag_quad=[]
    flag_quad_bin=[]
    #print (pair_terms,"pair terms",pair_list,"pair list")
    for i in range(len(pair_list)-1):
        if pair_list[i]!=[] and pair_list[i+1]!=[]:
            for k in range(len(pair_list[i])):
                temp=pair_list[i]
                for j in range(len(pair_list[i+1])):
                    boole,s1,s2=check_comb(temp[k],pair_list[i+1][j])
                    if boole:
                        x1=s1.count("1")
                        quad_list[x1].append(s1)
                        quad_terms[x1].append(pair_terms[i+1][j]+pair_terms[i][k])
                        flag_quad.append(pair_terms[i+1][j])
                        flag_quad.append(pair_terms[i][k])
                        flag_quad_bin.append(temp[k])
                        flag_quad_bin.append(pair_list[i+1][j])
    pi_terms=making_pi(flag_quad,pair_terms,pi_terms)
    #print (pair_list,"pair list",flag_quad_bin,"blahhhhhhh")
    for i in pair_list:
        for j in i:
            if j not in flag_quad_bin and j not in pi:
                pi.append(j)
    #pi=making_pi(flag_quad_bin,pair_list,pi)
    #print (pi,"pi")
    c3=quad_list.count([])
    for i in range(c3):
        quad_list.remove([])
        quad_terms.remove([])
    octet_terms=[[],[]]
    octet_list=[[],[]]
    flag_oct=[]
    flag_oct_bin=[]
    #print ("quad_terms",quad_terms)
    for i in range(len(quad_list)-1):
        if quad_list[i]!=[] and quad_list[i+1]!=[]:
            for k in range(len(quad_list[i])):
                temp=quad_list[i]
                for j in range(len(quad_list[i+1])):
                    boole,s1,s2=check_comb(temp[k],quad_list[i+1][j])
                    if boole:
                        x1=s1.count("1")
                        octet_list[x1].append(s1)
                        octet_terms[x1].append(quad_terms[i+1][j]+quad_terms[i][k])
                        flag_oct.append(quad_terms[i+1][j])
                        flag_oct.append(quad_terms[i][k])
                        flag_oct_bin.append(temp[k])
                        flag_oct_bin.append(quad_list[i+1][j])
    pi_terms=making_pi(flag_oct,quad_terms,pi_terms)
    for i in quad_list:
        for j in i:
            if j not in flag_oct_bin and j not in pi:
                pi.append(j)
    c4=octet_list.count([])
    for i in range(c4):
        octet_list.remove([])
        octet_terms.remove([])
    hex_terms=[]
    hex_list=[]
    flag_hex=[]
    flag_hex_bin=[]
    for i in range(len(octet_list)-1):
        if octet_list[i]!=[] and octet_list[i+1]!=[]:
            for k in range(len(octet_list)):
                temp=octet_list[i]
                for j in range(len(octet_list[i+1])):
                    boole,s1,s2=check_comb(temp[k],octet_list[i+1][j])
                    if boole:
                        hex_list.append(s1)
                        hex_terms.append(octet_terms[i+1][j]+octet_terms[i+1][k])
                        flag_hex.append(octet_terms[i+1][j])
                        flag_hex.append(octet_terms[i][k])
                        flag_hex_bin.append(temp[k])
                        flag_hex_bin.append(octet_list[i+1][j])
    pi_terms=making_pi(flag_hex,octet_terms,pi_terms)
    #print ("flag hex",flag_hex,"flag_hex_bin",flag_hex_bin)
    for i in octet_list:
        for j in i:
            if j not in flag_hex_bin and j not in pi:
                pi.append(j)
    if len(hex_list)!=0 and "----" in hex_list:
        return "1"
    #print ("pi terms hex",pi)
    #print ("hex list",hex_list)
    epi_table=[]
    top_row=["wxyz"]
    for i in pi_terms:
        for j in i:
            if j not in top_row and j not in dcterms:
                top_row.append(j)
    #print (top_row)
    epi_table.append(top_row)
    #print (pi_terms,"pi terms")
    #print (epi_table,"epi table")
    for i in range(1,len(pi)+1):
        l=[[pi[i-1],pi_terms[i-1]]]
        #print (l)
        for j in range(1,len(top_row)):
            #print (pi_terms[i-1])
            if epi_table[0][j] in pi_terms[i-1]:
                l.append(1)
            else:
                l.append(0)
        epi_table.append(l)
    #print (epi_table,"epi table")
    #print (pi,"pi.........")
    col_rem=[]
    row_rem=[]
    col_term_rem=[]
    for i in range(1,len(top_row)):
        count=0
        col=0
        row=0
        for j in range(1,len(pi)+1):
            if epi_table[j][i]==1:
                count+=1
                col=epi_table[j][0][0]
                col_term=epi_table[j][0][1]
                row=epi_table[0][i]
        if count==1:
            col_rem.append(col)
            col_term_rem.append(col_term)
            row_rem.append(row)
            if col not in epi:
                epi.append(col)
    #print (col_rem,"col_rem")
    #print (row_rem,"row_rem")
    #print ("new status")
    #print ("pi",pi)
    #print ("pi_terms",pi_terms)
    #print ("epi epi",epi)
    for i in col_rem:
        if len(pi)!=0 and i in pi:
            pi.remove(i)
    for i in col_term_rem:
        if len(pi_terms)!=0 and i in pi_terms:
            pi_terms.remove(i)
    for i in row_rem:
        if len(top_row)!=0 and i in top_row:
            top_row.remove(i)
    #print ("pi",pi)
    #print ("pi_terms",pi_terms)
    if len(pi)!=0:
        pi_table=[]
        pi_table.append(top_row)
        for i in range(1,len(pi)+1):
            l=[pi[i-1]]
            for j in range(1,len(top_row)):
                if pi_table[0][j] in pi_terms[i-1]:
                    l.append(1)
                else:
                    l.append(0)
            pi_table.append(l)
        #print (pi_table,"pi table")
        #print ("current status:")
        #print (pi,"pi final")
        #print (pi_terms,"pi terms final")
        #print (epi,"epi")
        counter=0
        expression=[]
        alias=[]
        
        for i in range(len(pi)):
            alias.append(chr(75+i))
        for i in range(len(pi_terms)-1):
            #print ("inside")
            l_compa=pi_terms[i]
            aly=alias[i]
            for j in range(i+1,len(pi_terms)):
                l_compi=pi_terms[j]
                aly2=alias[j]
                for k in l_compa:
                    if k in l_compi:
                        s=sorted(aly+aly2)
                        s="".join(s)
                        if s not in expression:
                            expression.append(s)
        #print (expression,"expression")
        term=[]
        if len(expression)!=0:
            expression2=[]
            for i in alias:
                element=[i]
                s=""
                if (len(expression)!=0):
                    for j in expression:
                        if i in j:
                            x=j.replace(i,"")
                            s=s+x
                            expression.remove(j)
                    element.append(s)
                    expression2.append(element)
            expression3=[]
            
            if len(expression2)!=1:
                if len(expression2)!=0:
                    term1=expression2[0]
                    term2=expression2[1]
                    
                    for i in term1:
                        for j in term2:
                            term.append(i+j)
                    expression2.remove(term1)
                    expression2.remove(term2)
                    while len(expression2)!=0:
                        term_2nd=expression2[0]
                        term_mult=term
                        term=[]
                        for i in term_mult:
                            for j in term_2nd:
                                term.append(i+j)
                        expression2.remove(term_2nd)
            else:
                for i in range(len(expression2[0])):
                    term.append(expression2[0][i])
            #print (term)
            for i in range(len(term)):
                ele=term[i]
                st=""
                for j in ele:
                    if j not in st:
                        st=st+j
                term[i]=st
        #print (term)
        if len(term)!=0:
            term.sort(key=len)
            #print (epi,"epi")
            ans_part=term[0]
            for i in ans_part:
                ind=alias.index(i)
                epi.append(pi[ind])
        #print ("epic", epi)
    final_ans_string=""
    for i in epi:
        #print(i,"termmmm")
        if numVar==4:
            for j in range(len(i)-1,-1,-1):
                
                if j==3:
                    
                    if i[j]=="1":
                        final_ans_string+="z"
                    elif i[j]=="0":
                        final_ans_string+="z\'"
                elif j==2:
                    if i[j]=="1":
                        final_ans_string+="y"
                    elif i[j]=="0":
                        final_ans_string+="y\'"
                elif j==1:
                    if i[j]=="1":
                        final_ans_string+="x"
                    elif i[j]=="0":
                        final_ans_string+="x\'"
                elif j==0:
                    if i[j]=="1":
                        final_ans_string+="w"
                    elif i[j]=="0":
                        final_ans_string+="w\'"
            final_ans_string+=" + "
        elif numVar==3:
            for j in range(len(i)-1,-1,-1):
                if j==2:
                    if i[j]=="1":
                        final_ans_string+="y"
                    elif i[j]=="0":
                        final_ans_string+="y\'"
                elif j==1:
                    if i[j]=="1":
                        final_ans_string+="x"
                    elif i[j]=="0":
                        final_ans_string+="x\'"
                elif j==0:
                    if i[j]=="1":
                        final_ans_string+="w"
                    elif i[j]=="0":
                        final_ans_string+="w\'"
            final_ans_string+=" + "
        elif numVar==2:
            for j in range(len(i)-1,-1,-1):
                if j==1:
                    if i[j]=="1":
                        final_ans_string+="x"
                    elif i[j]=="0":
                        final_ans_string+="x\'"
                elif j==0:
                    if i[j]=="1":
                        final_ans_string+="w"
                    elif i[j]=="0":
                        final_ans_string+="w\'"
            final_ans_string+=" + "
    
    final_ans_string=final_ans_string[0:len(final_ans_string)-3]
    if len(final_ans_string)==0:
        final_ans_string="1"
    return final_ans_string
    #for i in range(len(pi))
#print (minFunc(4,"(3,7,11,13,14,15) d -"))

        
            

            
        
    
    
    
    
            
            
        
        
    
                
            
    
            
    
    
                        
                        
            

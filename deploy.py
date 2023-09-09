# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:01:07 2023

@author: Tina
"""



import streamlit as st
import pandas as pd

import pickle 
user_id=pickle.load(open('user_id','rb'))
#user_id=pd.read_pickle('user_id_deploy')
#user_id=data['User-ID'].unique()
#user_id.sort()

kids=pickle.load(open('kids_deploy.csv','rb'))
young_adults=pickle.load(open('young_adults_deploy.csv','rb'))
adults=pickle.load(open('adults_deploy.csv','rb'))
elderly=pickle.load(open('elderly_deploy.csv','rb'))

indices_kids=pickle.load(open('indices_kids_deploy','rb'))

indices_young_adults=pickle.load(open('indices_young_adults_deploy','rb'))

indices_adults=pickle.load(open('indices_adults_deploy','rb'))

indices_elderly=pickle.load(open('indices_elderly_deploy','rb'))

knn=pickle.load(open('knn_kids_deploy.sav','rb'))
knn_young_adults=pickle.load(open('knn_young_adults_deploy.sav','rb'))
knn_adults=pickle.load(open('knn_adults_deploy.sav','rb'))
knn_elderly=pickle.load(open('knn_elderly_deploy.sav','rb'))


pt_user_kids=pickle.load(open('pt_user_kids_deploy','rb'))
pt_young_adults=pickle.load(open('pt_young_adults_deploy','rb'))
pt_adults=pickle.load(open('pt_adults_deploy','rb'))
pt_elderly=pickle.load(open('pt_elderly_deploy','rb'))
#pt_user_kids=kids.pivot_table(pt_user_kids)

#pt_user_kids.fillna(0,inplace=True)
pt_kids_copy=pt_user_kids.copy()
#-----------------


#pt_copy=pt.copy()
pt_young_adults_copy=pt_young_adults.copy()
#-----------



#pt_copy=pt.copy()
#----------------


#pt_copy=pt.copy()
pt_adults_copy=pt_adults.copy()
#--------------

#pt_copy=pt.copy()
#pt_elderly=pd.read_excel('elderly.xlsx')
pt_elderly_copy=pt_elderly.copy()

#########kids----------------------------------------------------------------------

def recomm_book_kids(user):
    
    books_read=[]
    
    rate_book_by_user=[]
    similarto_one_read=[]
    similarto=[]
    df_rate_book_by_user=pd.DataFrame(columns=['Book','Rate'])
    #similar=pd.DataFrame(columns='Book-Recommended')
    a=0
    #similar=pd.DataFrame(columns=['Similar_Book'])
    for m in pt_user_kids[pt_user_kids[user]>0][user].index.tolist():
        a=a+1
        books_read.append(m)
        rate_book_by_user.append(kids.loc[(kids['User-ID']==user) & 
                                        (kids['Book-Title']==m),
                                        ['Book-Title','Book-Rating']].iloc[0:].values[0:])


    for i in range(len(books_read)):
            df_rate_book_by_user=df_rate_book_by_user.append(pd.DataFrame(rate_book_by_user[i],
                                      columns=['Book','Rate']),ignore_index=True)
    df_rate_book_by_user=df_rate_book_by_user.sort_values(by='Rate',ascending=False)  
    #print("2 highest rated Books by user out of the books read by the user and the rating given  to each of it")
    if a>1:
        df_rate_book_by_user=df_rate_book_by_user.iloc[:2]
    #display(df_rate_book_by_user)
    

    for i in df_rate_book_by_user['Book']:
            index_for_book=pt_user_kids.index.tolist().index(i)
            similar_books=indices_kids[index_for_book].tolist()#getting tolist() so that in next we can get the index
            id_book=similar_books.index(index_for_book)
            similar_books.pop(id_book)#removing the read book by which similar books are found
            #print('similar to',i,'are',similar_books)
            for j in range(len(similar_books)): #similar books of each book read
                s=pt_user_kids.index[similar_books[j]]
                if a==1:
                    similarto_one_read.append(s)
                elif a>1:
                    if s not in similarto:
                        similarto.append(s)
                        if len(similarto)==3:
                            break



    similarto=similarto[:6]                
    if len(df_rate_book_by_user)==1:
        return(similarto_one_read)
    elif len(df_rate_book_by_user)>1:
        return(similarto)



#-------------------------second_young_adult

def recomm_book_young_adult(user):
    books_read=[]
    
    rate_book_by_user=[]
    similarto_one_read=[]
    similarto=[]
    df_rate_book_by_user=pd.DataFrame(columns=['Book','Rate'])
    #similar=pd.DataFrame(columns='Book-Recommended')
    a=0
    #similar=pd.DataFrame(columns=['Similar_Book'])
    for m in pt_young_adults[pt_young_adults[user]>0][user].index.tolist():
        a=a+1
        books_read.append(m)
        rate_book_by_user.append(young_adults.loc[(young_adults['User-ID']==user) & 
                                        (young_adults['Book-Title']==m),
                                        ['Book-Title','Book-Rating']].iloc[0:].values[0:])


    for i in range(len(books_read)):
            df_rate_book_by_user=df_rate_book_by_user.append(pd.DataFrame(rate_book_by_user[i],
                                      columns=['Book','Rate']),ignore_index=True)
    df_rate_book_by_user=df_rate_book_by_user.sort_values(by='Rate',ascending=False)  
   # print("2 highest rated Books by user out of the books read by the user and the rating given  to each of it")
    if a>1:
        df_rate_book_by_user=df_rate_book_by_user.iloc[:2]
    #display(df_rate_book_by_user)
    

    for i in df_rate_book_by_user['Book']:
            index_for_book=pt_young_adults.index.tolist().index(i)
            similar_books=indices_young_adults[index_for_book].tolist()#getting tolist() so that in next we can get the index
            id_book=similar_books.index(index_for_book)
            similar_books.pop(id_book)#removing the read book by which similar books are found
            #print('similar to',i,'are',similar_books)
            for j in range(len(similar_books)): #similar books of each book read
                s=pt_young_adults.index[similar_books[j]]
                if a==1:
                    similarto_one_read.append(s)
                elif a>1:
                    if s not in similarto:
                        similarto.append(s)
                        if len(similarto)==3:
                            break



    similarto=similarto[:6]                
    if len(df_rate_book_by_user)==1:
        return(similarto_one_read)
    elif len(df_rate_book_by_user)>1:
        return(similarto)

    
    #----------------adults----------------------
def recomm_book_adult(user):
    
    books_read=[]
    
    rate_book_by_user=[]
    similarto_one_read=[]
    similarto=[]
    df_rate_book_by_user=pd.DataFrame(columns=['Book','Rate'])
    #similar=pd.DataFrame(columns='Book-Recommended')
    a=0
    #similar=pd.DataFrame(columns=['Similar_Book'])
    for m in pt_adults[pt_adults[user]>0][user].index.tolist():
        a=a+1
        books_read.append(m)
        rate_book_by_user.append(adults.loc[(adults['User-ID']==user) & 
                                        (adults['Book-Title']==m),
                                        ['Book-Title','Book-Rating']].iloc[0:].values[0:])


    for i in range(len(books_read)):
            df_rate_book_by_user=df_rate_book_by_user.append(pd.DataFrame(rate_book_by_user[i],
                                      columns=['Book','Rate']),ignore_index=True)
    df_rate_book_by_user=df_rate_book_by_user.sort_values(by='Rate',ascending=False)  
    #print("2 highest rated Books by user out of the books read by the user and the rating given  to each of it")
    if a>1:
        df_rate_book_by_user=df_rate_book_by_user.iloc[:2]
    #display(df_rate_book_by_user)
    

    for i in df_rate_book_by_user['Book']:
            index_for_book=pt_adults.index.tolist().index(i)
            similar_books=indices_adults[index_for_book].tolist()#getting tolist() so that in next we can get the index
            id_book=similar_books.index(index_for_book)
            similar_books.pop(id_book)#removing the read book by which similar books are found
            #print('similar to',i,'are',similar_books)
            for j in range(len(similar_books)): #similar books of each book read
                s=pt_adults.index[similar_books[j]]
                if a==1:
                    similarto_one_read.append(s)
                elif a>1:
                    if s not in similarto:
                        similarto.append(s)
                        if len(similarto)==3:
                            break



    similarto=similarto[:6]                
    if len(df_rate_book_by_user)==1:
        return(similarto_one_read)
    elif len(df_rate_book_by_user)>1:
        return(similarto)


 #---------------elderly   
 
def recomm_book_elderly(user):
    
    
    books_read=[]
    
    rate_book_by_user=[]
    similarto_one_read=[]
    similarto=[]
    df_rate_book_by_user=pd.DataFrame(columns=['Book','Rate'])
    #similar=pd.DataFrame(columns='Book-Recommended')
    a=0
    #similar=pd.DataFrame(columns=['Similar_Book'])
    for m in pt_elderly[pt_elderly[user]>0][user].index.tolist():
        a=a+1
        books_read.append(m)
        rate_book_by_user.append(elderly.loc[(elderly['User-ID']==user) & 
                                        (elderly['Book-Title']==m),
                                        ['Book-Title','Book-Rating']].iloc[0:].values[0:])


    for i in range(len(books_read)):
            df_rate_book_by_user=df_rate_book_by_user.append(pd.DataFrame(rate_book_by_user[i],
                                      columns=['Book','Rate']),ignore_index=True)
    df_rate_book_by_user=df_rate_book_by_user.sort_values(by='Rate',ascending=False)  
    #print("2 highest rated Books by user out of the books read by the user and the rating given  to each of it")
    if a>1:
        df_rate_book_by_user=df_rate_book_by_user.iloc[:2]
    
    

    for i in df_rate_book_by_user['Book']:
            index_for_book=pt_elderly.index.tolist().index(i)
            similar_books=indices_elderly[index_for_book].tolist()#getting tolist() so that in next we can get the index
            id_book=similar_books.index(index_for_book)
            similar_books.pop(id_book)#removing the read book by which similar books are found
            print('similar to',i,'are',similar_books)
            for j in range(len(similar_books)): #similar books of each book read
                s=pt_elderly.index[similar_books[j]]
                if a==1:
                    similarto_one_read.append(s)
                elif a>1:
                    if s not in similarto:
                        similarto.append(s)
                        if len(similarto)==3:
                            break



    similarto=similarto[:6]                
    if len(df_rate_book_by_user)==1:
        return(similarto_one_read)
    elif len(df_rate_book_by_user)>1:
        return(similarto)


    
    

def main():
    st.title("Book Recommender System")
    
   
    selected_user=st.sidebar.selectbox("User-ID",user_id['User-ID'])
    #st.write("Age:",data[data['User-ID']==selected_user]['Age'].values[0])
    #st.write("Country :",data[data['User-ID']==selected_user]['Country'].values[0])
    
    if st.button("Recommend"):
        st.write("Recommendation of Books to the user ",selected_user   )
        
        age= user_id[user_id['User-ID']==selected_user]['Age'].values[0] 
        if age<26:
                
            #if data['User-ID']==selected_user and data['Age']<21:
                
            #recommendation=data['Age'].apply(lambda x: recomm_book_kids(selected_user) if x < 21 else "False")
            recommendation=recomm_book_kids(selected_user)
            col1, col2,col3 = st.columns((1,1,1)) 
            #with st.container:
                
            with col1:
                    st.write(recommendation[0])
                    st.image(kids[kids['Book-Title']==recommendation[0]]['Image-URL-M'].values[0])
                    st.write(recommendation[3])
                    st.image(kids[kids['Book-Title']==recommendation[3]]['Image-URL-M'].values[0])
            #with st.container:     
            with col2:
                    st.write(recommendation[1])
                    st.image(kids[kids['Book-Title']==recommendation[1]]['Image-URL-M'].values[0])
                    st.write(recommendation[4])
                    st.image(kids[kids['Book-Title']==recommendation[4]]['Image-URL-M'].values[0])
           # with st.container:       
            with col3:
                    st.write(recommendation[2])
                    st.image(kids[kids['Book-Title']==recommendation[2]]['Image-URL-M'].values[0])
                    st.write(recommendation[5])
                    st.image(kids[kids['Book-Title']==recommendation[5]]['Image-URL-M'].values[0])
                    
       
        
        if (age>25) & (age<37):
                 
             #if data['User-ID']==selected_user and data['Age']<21:
                 
             #recommendation=data['Age'].apply(lambda x: recomm_book_kids(selected_user) if x < 21 else "False")
             recommendation=recomm_book_young_adult(selected_user)
             col1, col2,col3 = st.columns((1,1,1)) 
             #with st.container:
                 
             with col1:
                     st.write(recommendation[0])
                     st.image(young_adults[young_adults['Book-Title']==recommendation[0]]['Image-URL-M'].values[0])
                     st.write(recommendation[3])
                     st.image(young_adults[young_adults['Book-Title']==recommendation[3]]['Image-URL-M'].values[0])
             #with st.container:     
             with col2:
                     st.write(recommendation[1])
                     st.image(young_adults[young_adults['Book-Title']==recommendation[1]]['Image-URL-M'].values[0])
                     st.write(recommendation[4])
                     st.image(young_adults[young_adults['Book-Title']==recommendation[4]]['Image-URL-M'].values[0])
            # with st.container:       
             with col3:
                     st.write(recommendation[2])
                     st.image(young_adults[young_adults['Book-Title']==recommendation[2]]['Image-URL-M'].values[0])
                     st.write(recommendation[5])
                     st.image(young_adults[young_adults['Book-Title']==recommendation[5]]['Image-URL-M'].values[0])
                    
        
        if (age>36) & (age<=50):
                 
             #if data['User-ID']==selected_user and data['Age']<21:
                 
             #recommendation=data['Age'].apply(lambda x: recomm_book_kids(selected_user) if x < 21 else "False")
             recommendation=recomm_book_adult(selected_user)
             col1, col2,col3 = st.columns((1,1,1)) 
             #with st.container:
                 
             with col1:
                     st.write(recommendation[0])
                     st.image(adults[adults['Book-Title']==recommendation[0]]['Image-URL-M'].values[0])
                     st.write(recommendation[3])
                     st.image(adults[adults['Book-Title']==recommendation[3]]['Image-URL-M'].values[0])
             #with st.container:     
             with col2:
                     st.write(recommendation[1])
                     st.image(adults[adults['Book-Title']==recommendation[1]]['Image-URL-M'].values[0])
                     st.write(recommendation[4])
                     st.image(adults[adults['Book-Title']==recommendation[4]]['Image-URL-M'].values[0])
            # with st.container:       
             with col3:
                     st.write(recommendation[2])
                     st.image(adults[adults['Book-Title']==recommendation[2]]['Image-URL-M'].values[0])
                     st.write(recommendation[5])
                     st.image(adults[adults['Book-Title']==recommendation[5]]['Image-URL-M'].values[0])
                     
        if age>=51:
                  
              #if data['User-ID']==selected_user and data['Age']<21:
                  
              #recommendation=data['Age'].apply(lambda x: recomm_book_kids(selected_user) if x < 21 else "False")
              recommendation=recomm_book_elderly(selected_user)
              col1, col2,col3 = st.columns((1,1,1)) 
              #with st.container:
                  
              with col1:
                      st.write(recommendation[0])
                      st.image(elderly[elderly['Book-Title']==recommendation[0]]['Image-URL-M'].values[0])
                      st.write(recommendation[3])
                      st.image(elderly[elderly['Book-Title']==recommendation[3]]['Image-URL-M'].values[0])
              #with st.container:     
              with col2:
                      st.write(recommendation[1])
                      st.image(elderly[elderly['Book-Title']==recommendation[1]]['Image-URL-M'].values[0])
                      st.write(recommendation[4])
                      st.image(elderly[elderly['Book-Title']==recommendation[4]]['Image-URL-M'].values[0])
             # with st.container:       
              with col3:
                      st.write(recommendation[2])
                      st.image(elderly[elderly['Book-Title']==recommendation[2]]['Image-URL-M'].values[0])
                      st.write(recommendation[5])
                      st.image(elderly[elderly['Book-Title']==recommendation[5]]['Image-URL-M'].values[0])
                      
                
           
    
        
if __name__=='__main__':
    main()
    
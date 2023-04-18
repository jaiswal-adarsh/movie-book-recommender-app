import streamlit as st

def intro():
    import streamlit as st
    st.snow()

    st.write("# Welcome to Recommendation System! 👋")
    st.sidebar.success("Select a recommender above.")

    st.markdown(
        """
        Enhance your experience and discover more relevant content with the power of personalized recommendations - made possible by the cutting-edge technology of recommendation systems.

        **👈 Select a recommender from the dropdown on the left** to experience the magic of the Recommendation System!

        ### Movie Recommender

        - It is a context-based movie recommender is a type of recommendation system that suggests movies to users based on the context in which they plan to watch the movie. This could include factors such as the time of day, the user's location, the weather, or the user's mood.

        - The system uses algorithms to analyze the context data and identify patterns that can help it predict what movies may be appropriate for the user at that particular moment. For example, if it's a rainy day, the system might recommend movies with a cozy or comforting atmosphere. If the user is watching a movie late at night, the system might recommend movies that are less intense and more relaxing.

        - Context-based movie recommenders can enhance the user experience by providing more personalized and relevant movie recommendations. It can also help users discover new movies that they might not have considered watching otherwise. This type of recommendation system can be used by movie streaming services or other platforms to increase user engagement and retention.

        ### Book Recommender

        - It is an author-based book recommender is a type of recommendation system that suggests books to users based on their favorite authors or similar authors. The system uses algorithms to analyze book data and identify patterns that can help it predict what other books the user may be interested in based on their preferred author.

        - The author-based book recommender system relies on content-based filtering approach, which uses book features such as genre, themes, writing style, and plot to recommend similar books written by the same author or authors with a similar writing style.

        - This type of book recommender system is useful for readers who have a particular author they enjoy and want to explore other books by the same author or authors with a similar style. It can be used by online bookstores, e-readers, and other book-related platforms to help users discover new books and authors they may not have considered otherwise.

        - Overall, the goal of an author-based book recommender is to enhance the user experience by providing personalized and relevant book recommendations that match the user's reading preferences.
    """
    )

def books_recommender():
    import requests
    import streamlit as st
    import pickle
    import pandas as pd
    import time

    # def fetch_poster(movie_id):
    #     response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    #     data= response.json()
    #
    #     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

    def recommend(book):
        book_index = books[books['b_title'] == book].index[0]
        distances = similarity[book_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]

        recommended_book = []
        # book_author=[]
        # recommended_movies_poster=[]

        for i in movies_list:
            ISBN = books.iloc[i[0]].ISBN
            recommended_book.append(books.iloc[i[0]].b_info)
            # book_author.append(books.iloc[i[0]].b_author)
            # fetch poster from api
            # recommended_movies_poster.append(fetch_poster(movie_id))
        return recommended_book

    books_dict = pickle.load(open('book_dict.pkl', 'rb'))
    books = pd.DataFrame(books_dict)

    similarity = pickle.load(open('book_similarity.pkl', 'rb'))

    st.title('Books Recommender! 📖')
    st.snow()
    selected_book_name = st.selectbox(
        'Enter the name of the book',
        books['b_title'].values)

    if st.button('Recommend'):
        with st.spinner('Wait for it...'):
            time.sleep(2)
        st.success('Done!')

        names = recommend(selected_book_name)
        # author = recommend(selected_book_name)

        for i in range(10):
            st.header('👉 '+ names[i])
            # st.markdown(author[i])


def movies_recommender():
    import requests
    import streamlit as st
    import pickle
    import pandas as pd
    import time

    def fetch_poster(movie_id):
        response = requests.get(
            'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
                movie_id))
        data = response.json()

        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]

        recommended_movies = []
        recommended_movies_poster = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            # fetch poster from api
            recommended_movies_poster.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_poster

    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open('similarity.pkl', 'rb'))

    st.title('Movies Recommender! 🎞️')
    st.snow()
    selected_movie_name = st.selectbox(
        'Enter the name of the movie',
        movies['title'].values)

    if st.button('Recommend'):
        with st.spinner('Wait for it...'):
            time.sleep(2)
        st.success('Done!')

        names, posters = recommend(selected_movie_name)

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.markdown(names[0])
            st.image(posters[0])

        with col2:
            st.markdown(names[1])
            st.image(posters[1])

        with col3:
            st.markdown(names[2])
            st.image(posters[2])

        with col4:
            st.markdown(names[3])
            st.image(posters[3])

        with col5:
            st.markdown(names[4])
            st.image(posters[4])

        col6, col7, col8, col9, col10 = st.columns(5)

        with col6:
            st.markdown(names[5])
            st.image(posters[5])

        with col7:
            st.markdown(names[6])
            st.image(posters[6])

        with col8:
            st.markdown(names[7])
            st.image(posters[7])

        with col9:
            st.markdown(names[8])
            st.image(posters[8])

        with col10:
            st.markdown(names[9])
            st.image(posters[9])

        # for i in recommendations:
        #     st.write(i)




page_names_to_funcs = {
    "Dashboard": intro,
    "Movies Recommender": movies_recommender,
    "Books Recommender": books_recommender,

}

demo_name = st.sidebar.selectbox("Select a recommender", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
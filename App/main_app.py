import streamlit as st
import pandas as pd
import joblib
import os
import base64

# Set background function
def set_background(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            bg_image = f.read()
        bg_image_encoded = base64.b64encode(bg_image).decode('utf-8')
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url("data:image/jpg;base64,{bg_image_encoded}");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Background image not found. Please check the file path.")


# Set the background image
set_background("football_dashboard.jpg")  

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar buttons for navigation
def styled_sidebar_button(label, page):
    if st.sidebar.button(label):
        st.session_state.page = page

# Sidebar buttons
st.sidebar.title("Football Dashboard")
styled_sidebar_button("🏠 Home", "Home")
styled_sidebar_button("⚽ Competition", "Competition")
styled_sidebar_button("📋 Match", "Match")
styled_sidebar_button("👤 Football Player", "Player")
styled_sidebar_button("📊 XG Prediction", "XG")

# Load pre-trained model and preprocessor
preprocessor = joblib.load("preprocessor.pkl")
model = joblib.load("gradient_boosting_model.pkl")

# Home Page
def show_home_page():
    st.title("Welcome to the Football Dashboard")
    
    st.markdown(
        """
        This dashboard is designed to provide insights into football data with detailed visualizations and analysis.  
        
        ### Features:
        - **Competitions**: Explore team performances and statistics from major tournaments.
        - **Matches**: Delve into specific match data, including goals, shots, and xG analysis.
        - **Players**: Analyze individual player statistics and their contributions.
        - **Expected Goals (XG) Prediction**: Use advanced models to predict the likelihood of scoring based on various factors.

        ### Why Use This Dashboard?
        Gain a deeper understanding of football dynamics through data-driven insights. Whether you're a fan, analyst, or coach, this tool will help you make informed observations.

        **Navigate using the sidebar to explore different sections!**
        """
    )


# Competition Page
def show_competition_page():
    st.title("Competition Analysis")
    st.subheader("Visualizations for the 2019 FIFA Women's World Cup")
    
    st.write("""
    This page presents key statistics and insights from the **2019 FIFA Women's World Cup**, including the performance 
    of various teams in terms of wins, draws, losses, and goal differences.
    """)

    # Displaying the first figure: Number of Wins, Draws, Losses per Team
    st.header("Number of Wins, Draws, Losses per Team")
    st.image("competition1.jpg", caption="Number of Wins, Draws, Losses per Team", use_container_width=True)

    # Adding space between figures
    st.write("\n")  # Adds a newline between figures
    
    # Displaying the second figure: Goal Differences per Team
    st.header("Goal Differences per Team")
    st.image("competition2.jpg", caption="Goal Differences per Team",use_container_width=True)

# Match Page
def show_match_page():
    # Title and subtitle for the page
    st.title("Match Analysis")
    st.subheader("Data Analysis and Data Visualization for the Women's World Cup 2019 Final Match")
    st.write("**Match ID:** 69321")

    # Team 1: The United States Women's
    st.markdown("### Team 1: The United States Women's")
    st.image("usa.jpg", caption="The United States Women's Team", use_container_width=True)  

    # Shot Map with xG and Shot Technique
    st.markdown("### Shot Map with xG and Shot Technique")
    st.image("shotmap1.jpg", caption="Shot Map with Expected Goals (xG) and Shot Technique", use_container_width=True)  

    # Shot Body Part Distribution
    st.markdown("### Shot Body Part Distribution")
    st.image("bodypart1.jpg", caption="Distribution of Shots by Body Part", use_container_width=True)  

    # xG Over Time
    st.markdown("### xG Over Time")
    st.image("xg1.jpg", caption="Expected Goals (xG) Over Time", use_container_width=True)  

    st.write(
        """
        This line plot highlights the moments when the team had significant scoring opportunities (high xG values) and 
        when their offensive pressure increased or decreased. The xG is tracked at each minute, showing how the team's 
        attacking efforts were spread across the match and helping to identify key moments that contributed to their 
        overall offensive performance.

        The plot provides valuable insights into the dynamics of the match, allowing us to analyze the flow of attacks 
        and the quality of chances created by the United States Women's team during the 2019 Women's World Cup final.
        """
    )



    # Team 2: The Netherlands Women's
    st.markdown("### Team 2: The Netherlands Women's")
    st.image("netherlands.jpg", caption="The Netherlands Women's", use_container_width=True)  

    # Shot Map with xG and Shot Technique
    st.markdown("### Shot Map with xG and Shot Technique")
    st.image("shotmap2.jpg", caption="Shot Map with Expected Goals (xG) and Shot Technique", use_container_width=True)  

    # Shot Body Part Distribution
    st.markdown("### Shot Body Part Distribution")
    st.image("bodypart2.jpg", caption="Distribution of Shots by Body Part", use_container_width=True)  

    # xG Over Time
    st.markdown("### xG Over Time")
    st.image("xg2.jpg", caption="Expected Goals (xG) Over Time", use_container_width=True)  

    st.write(
        """
        This line plot highlights the moments when the team had significant scoring opportunities (high xG values) and 
        when their offensive pressure increased or decreased. The xG is tracked at each minute, showing how the team's 
        attacking efforts were spread across the match and helping to identify key moments that contributed to their 
        overall offensive performance.

        The plot provides valuable insights into the dynamics of the match, allowing us to analyze the flow of attacks 
        and the quality of chances created by the United States Women's team during the 2019 Women's World Cup final.
        """
    )
    st.markdown("### Comparison of xG by Time: United States Women's vs Netherlands Women's")
    st.image("compare.jpg", caption="Comparison of Expected Goals (xG) Over Time", use_container_width=True)

    st.write(
        """
        This line plot compares the Expected Goals (xG) over time for the United States Women's team and their opponent in 
        the 2019 Women's World Cup final. The United States consistently outperforms the opponent, with a higher xG 
        throughout the match, indicating more and better quality scoring chances. This highlights their attacking dominance 
        and superior performance in creating goal-scoring opportunities during the game.
        """
    )

    # Conclusion
    st.write(
        """
        At the conclusion of my analysis, I turn to Expected Goals (xG), a crucial metric in modern football analytics. 
        The xG value measures the probability of a shot turning into a goal based on several factors, including shot type, 
        position, and game context. 

        By analyzing xG data, I can assess whether the result of the match was consistent with the quality of the chances 
        created by both teams, offering a more objective perspective on the final outcome.
        """
    )
    


# Football Player Page
def show_football_player_page():
    st.title("Football Player Analysis")

    # My Favorite Player
    st.markdown("## My Favourite Player: Alex Morgan")
    st.image("alexmorgan.jpg", caption="Alex Morgan", use_container_width=True)  

    # Histogram with KDE for Shot xG Values
    st.markdown("### Distribution of Shot xG Values")
    st.image("xgalex.jpg", caption="Histogram with KDE of Shot xG Values", use_container_width=True)  
    st.write(
        """
        This histogram with a Kernel Density Estimate (KDE) visualizes the distribution of Expected Goals (xG) values for 
        shots taken by Alex Morgan. It highlights the range and frequency of xG values, helping us understand the quality 
        of scoring opportunities she had during the analyzed matches.
        """
    )

    # Pass Completion Percentage Visualization
    st.markdown("### Pass Completion Percentage")
    st.image("alexpasses.jpg", caption="Pass Completion Percentage Visualization", use_container_width=True)  
    st.write(
        """
        This visualization represents Alex Morgan's pass completion percentage during the analyzed matches. It provides 
        insights into her ability to connect passes effectively, a crucial aspect of her role as a forward in the team.
        """
    )
    # Analysis for Megan Anna Rapinoe
    st.markdown("## Analysis for Megan Anna Rapinoe")
    
    # Pass Network on the Pitch for Megan Rapinoe
    st.markdown("### Pass Network on the Pitch")
    st.image("meganpitch.jpg", caption="Pass Network Visualization on the Pitch", use_column_width=True) 
    st.write(
        """
        This visualization illustrates Megan Rapinoe's pass network during the match, showing connections with teammates 
        and the areas of the pitch where she was most involved. It provides insights into her role in the team's buildup play 
        and overall attacking strategy.
        """
    )

    # Pass Completion Percentage for Megan Rapinoe
    st.markdown("### Pass Completion Percentage (Megan Anna Rapinoe)")
    st.image("meganpasses.jpg", caption="Pass Completion Percentage Visualization", use_container_width=True) 
    st.write(
        """
        This visualization shows Megan Rapinoe's pass completion percentage during the final match, 
        emphasizing her effectiveness in maintaining possession and supporting her teammates.
        """
    )

    






def show_xg_prediction_page(preprocessor, model):
    st.title("📊 Expected Goals (XG) Prediction")

    # Inputs for numerical features
    location_x = st.text_input("Enter Location X (e.g., 88.7):")
    location_y = st.text_input("Enter Location Y (e.g., 55.6):")
    end_loc_x = st.text_input("Enter End Location X (e.g., 100.2):")
    end_loc_y = st.text_input("Enter End Location Y (e.g., 50.8):")
    end_loc_z = st.text_input("Enter End Location Z (e.g., 0):")

    # Categorical features
    play_pattern = st.selectbox("Play Pattern", ["From Free Kick", "Regular Play", "From Corner", "Set Piece"])
    position = st.selectbox("Position", ["Right Center Midfield", "Striker", "Left Back", "Goalkeeper"])
    shot_body_part = st.selectbox("Shot Body Part", ["Left Foot", "Right Foot", "Head"])
    shot_outcome = st.selectbox("Shot Outcome", ["Blocked", "Saved", "Goal", "Off Target"])
    shot_technique = st.selectbox("Shot Technique", ["Normal", "Volley", "Chip"])
    shot_type = st.selectbox("Shot Type", ["Free Kick", "Penalty", "Open Play"])
    under_pressure = st.radio("Under Pressure?", ["Yes", "No"])

    if st.button("Predict XG"):
        # Validate numerical inputs
        try:
            location_x = float(location_x)
            location_y = float(location_y)
            end_loc_x = float(end_loc_x)
            end_loc_y = float(end_loc_y)
            end_loc_z = float(end_loc_z)
        except ValueError:
            st.error("Please enter valid numbers for the location fields.")
            return

        # Convert categorical and binary features
        under_pressure_binary = 1 if under_pressure == "Yes" else 0

        # Prepare input data
        input_data = pd.DataFrame({
            'location_x': [location_x],
            'location_y': [location_y],
            'end_loc_x': [end_loc_x],
            'end_loc_y': [end_loc_y],
            'end_loc_z': [end_loc_z],
            'play_pattern': [play_pattern],
            'position': [position],
            'shot_body_part': [shot_body_part],
            'shot_outcome': [shot_outcome],
            'shot_technique': [shot_technique],
            'shot_type': [shot_type],
            'under_pressure': [under_pressure_binary]
        })
        st.write("Input Data:")
        st.write(input_data)

        # Preprocess input data and predict
        try:
            input_data_processed = preprocessor.transform(input_data)
            prediction = model.predict(input_data_processed)[0]
            st.markdown(
                f"""
                <div style='
                    background-color: #f0f0f5;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    color: #333;
                    '>
                    Predicted XG: {prediction:.4f}
                </div>
                """, 
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")




# Display the correct page based on session state
if st.session_state.page == "Home":
    show_home_page()
elif st.session_state.page == "Competition":
    show_competition_page()
elif st.session_state.page == "Match":
    show_match_page()
elif st.session_state.page == "Player":
    show_football_player_page()
elif st.session_state.page == "XG":
    show_xg_prediction_page(preprocessor, model)

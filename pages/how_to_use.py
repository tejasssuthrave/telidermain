import streamlit as st

def show_how_to_use():
    """Display instructions on how to use the application."""
    
    # Page header
    st.markdown(
        f"<h1 style='color: #611e9e; text-align: center;'>❓ How to Use TelidermAI</h1>", 
        unsafe_allow_html=True
    )
    
    # Introduction
    st.markdown(
        """
        <p style='font-size: 18px; text-align: center;'>
            This guide will help you navigate and get the most out of TeledermAI's features.
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # Image Prediction section
    st.markdown(
        f"<h2 style='color: #611e9e;'>📷 Using the Image Prediction Feature</h2>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <ol style='font-size: 16px;'>
            <li><strong>Navigate to the Predict page</strong> using the navigation bar at the top.</li>
            <li><strong>Upload an image</strong> of the skin condition you want to analyze.</li>
            <li>Ensure the image is <strong>clear, well-lit, and focused</strong> on the skin condition.</li>
            <li>The system will process the image and display the <strong>top predicted conditions</strong> along with confidence levels.</li>
            <li><strong>Review the results</strong> and consider consulting a healthcare professional for proper diagnosis.</li>
        </ol>
        
        <div style='background-color: #f8f9fa; padding: 15px; border-left: 5px solid #611e9e; margin: 15px 0;'>
            <strong>Pro tip:</strong> For best results, take photos in natural daylight without flash, and make sure the 
            skin condition is clearly visible and not obscured by hair, clothing, or shadows.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # PDF Chat section
    st.markdown(
        f"<h2 style='color: #611e9e;'>💬 Using the Chat with PDF Feature</h2>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <ol style='font-size: 16px;'>
            <li><strong>Navigate to the Chat with PDF page</strong> using the navigation bar at the top.</li>
            <li><strong>Upload one or more PDF documents</strong> containing dermatology information.</li>
            <li>Click the <strong>"Process PDFs for Chat"</strong> button and wait for processing to complete.</li>
            <li>Once processing is complete, <strong>type your question</strong> in the text input field.</li>
            <li>The AI will <strong>analyze the documents</strong> and provide an answer based on their content.</li>
            <li>You can continue asking questions and <strong>view your conversation history</strong> below.</li>
        </ol>
        
        <div style='background-color: #f8f9fa; padding: 15px; border-left: 5px solid #611e9e; margin: 15px 0;'>
            <strong>Pro tip:</strong> Ask specific questions to get more precise answers. For example, instead of 
            "Tell me about eczema," try "What are the common treatments for eczema mentioned in the document?"
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Best Practices section
    st.markdown(
        f"<h2 style='color: #611e9e;'>✅ Best Practices</h2>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <ul style='font-size: 16px;'>
            <li><strong>Image Quality Matters:</strong> Clear, well-lit images lead to more accurate predictions.</li>
            <li><strong>Multiple Angles:</strong> Consider uploading multiple images of the same condition from different angles.</li>
            <li><strong>Relevant PDFs:</strong> Upload PDFs that are specifically related to your area of interest for better chat responses.</li>
            <li><strong>Verify Information:</strong> Always cross-check the information with reliable medical sources.</li>
            <li><strong>Consult Professionals:</strong> Use TeledermAI as a preliminary tool, not a replacement for professional medical advice.</li>
        </ul>
        """, 
        unsafe_allow_html=True
    )
    
    # Video Tutorial Section
    st.markdown(
        f"<h2 style='color: #611e9e;'>🎥 Video Tutorial</h2>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style='font-size: 16px;'>
            Watch our video tutorial to get a comprehensive overview of TelidermAI's features and how to use them effectively.
        </p>
        """, 
        unsafe_allow_html=True
    )

    # Video Tutorial Section
    st.markdown(
        f"<h2 style='color: #611e9e;'>🎥 Video Tutorial</h2>", 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='font-size: 16px;'>
            Watch our video tutorial to get a comprehensive overview of TelidermAI's features and how to use them effectively.
        </p>
        """, 
        unsafe_allow_html=True
    )

    # Embedded YouTube video tutorial
    st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")  # <-- Replace with actual link


    # Video Tutorial Section
    
    # Placeholder for video tutorial - to be added by user later
    # st.markdown(
    #     """
    #     <div style="background-color: #f0f2f6; padding: 20px; border-radius: 5px; margin: 15px 0; text-align: center;">
    #         <p style="font-size: 18px; margin-bottom: 10px;">🎬 Video tutorial will be available soon!</p>
    #         <p style="color: #555;">Check back later for a comprehensive walkthrough of all features.</p>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )
    
    # # Getting help section
    # st.markdown(
    #     f"<h2 style='color: #611e9e;'>🆘 Getting Help</h2>", 
    #     unsafe_allow_html=True
    # )
    
    # st.markdown(
    #     """
    #     <p style='font-size: 16px;'>
    #         If you encounter any issues or have questions about using TeledermAI, please visit our Contact Us page 
    #         or reach out to our team via email at <a href="mailto:tejassuthrave@gmail.com">tejassuthrave@gmail.com</a>.
    #     </p>
    #     """, 
    #     unsafe_allow_html=True
    # )

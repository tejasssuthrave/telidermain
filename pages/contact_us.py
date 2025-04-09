import streamlit as st

def get_base64_of_contact_icon():
    # This is a placeholder function for compatibility
    return ""

def show_contact_us():
    """Display contact information and a simple contact form."""
    
    # Page header
    st.markdown(
        f"<h1 style='color: #611e9e; text-align: center;'>📞 Contact Us</h1>", 
        unsafe_allow_html=True
    )
    
    # Introduction
    st.markdown(
        """
        <p style='font-size: 18px; text-align: center;'>
            Have questions, feedback, or need assistance? We're here to help!
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # Create two columns
    col1, col2 = st.columns([1, 1])
    
    # Contact information
    with col1:
        st.markdown(
            f"<h2 style='color: #611e9e;'>Contact Information</h2>", 
            unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
                <h3 style='color: #611e9e; margin-top: 0;'>Development Team</h3>
                <p><strong>📧 Email:</strong> <a href="mailto:tejassuthrave@gmail.com">telidermai@gmail.com</a></p>
                <p><strong>🔗 GitHub:</strong> <a href="https://github.com/123-rishi/Teliderm-Ai" target="_blank">GitHub Repository</a></p>
                <p><strong>🤗 Hugging Face:</strong> <a href="https://huggingface.co/TelidermAI" target="_blank">TelidermAI Models</a></p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px;'>
                <h3 style='color: #611e9e; margin-top: 0;'>Email Us</h3>
                <p><strong>🛠️ Support:</strong> <a href="mailto:support@telidermai.com">support@telidermai.com</a></p>
                <p><strong>ℹ️ Info:</strong> <a href="mailto:info@telidermai.com">info@telidermai.com</a></p>
                <p><strong>💬 Feedback:</strong> <a href="mailto:feedback@telidermai.com">feedback@telidermai.com</a></p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Contact form
    with col2:
        st.markdown(
            f"<h2 style='color: #611e9e;'>Send Us a Message</h2>", 
            unsafe_allow_html=True
        )
        
        # Just add styling for the form fields without changing the structure
        st.markdown(
            """
            <style>
            /* Just improve form field styling without changing layout */
            div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea {
                border: 1px solid #611e9e !important;
                border-radius: 8px !important;
            }
            div[data-testid="stTextInput"] input:focus, div[data-testid="stTextArea"] textarea:focus {
                border-color: #8149b5 !important;
                box-shadow: 0 0 0 2px rgba(97, 30, 158, 0.2) !important;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )
        
        # Original form structure from extracted/TelidermAI_App/pages/contact_us.py
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.selectbox(
            "Subject", 
            [
                "General Inquiry", 
                "Technical Support", 
                "Feedback", 
                "Bug Report", 
                "Feature Request", 
                "Other"
            ]
        )
        message = st.text_area("Message", height=150)
        
        # Original submit button
        if st.button("Submit"):
            if name and email and message:
                # This would normally connect to a backend service to send the message
                # For now, just display a success message
                st.success(
                    "Thank you for your message! Our team will get back to you as soon as possible. "
                    "Please note that this is a demo contact form and doesn't actually send messages."
                )
            else:
                st.error("Please fill in all required fields (Name, Email, and Message).")
    
    # FAQ section
    st.markdown(
        f"<h2 style='color: #611e9e; text-align: center; margin-top: 30px;'>Frequently Asked Questions</h2>", 
        unsafe_allow_html=True
    )
    
    # FAQ items
    faq_items = [
        {
            "question": "Is TelidermAI a substitute for professional medical advice?",
            "answer": "No, TelidermAI is designed to provide preliminary information and analysis only. It is not intended to replace professional medical diagnosis or treatment. Always consult with a qualified healthcare provider for proper evaluation and diagnosis."
        },
        {
            "question": "How accurate are the predictions from TelidermAI?",
            "answer": "While our model achieves a high accuracy rate on our test dataset, it should be considered as a preliminary screening tool. The accuracy may vary depending on image quality, lighting conditions, and the specific skin condition being analyzed."
        },
        {
            "question": "How is my data handled when I upload images or PDFs?",
            "answer": "TelidermAI processes images and PDFs directly in your browser session. We do not permanently store your uploaded images or documents on our servers. All processing is done temporarily for the purpose of providing analysis and responses."
        },
        {
            "question": "Can I use TelidermAI on mobile devices?",
            "answer": "Yes, TelidermAI is designed to be responsive and works on most modern mobile devices. You can upload images directly from your smartphone's camera or gallery."
        }
    ]
    
    # Display FAQ items as expandable sections
    for i, faq in enumerate(faq_items):
        with st.expander(f"Q: {faq['question']}"):
            st.write(f"A: {faq['answer']}")

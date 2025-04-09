def load_css():
    """Load custom CSS styles for the application."""
    return """
    <style>
        /* Hide info icons and boxes */
        .stAlert, .streamlit-expanderHeader {
            display: none !important;
        }
        
        /* Remove blue gradient bar below navigation */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1px;
            background-color: transparent !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: auto;
            background-color: transparent !important;
            border-radius: 4px 4px 0 0;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        
        /* Hide all blue info boxes and their icons */
        .st-emotion-cache-16txtl3, .st-emotion-cache-r421ms, .stInfo {
            display: none !important;
        }
        
        /* Hide info icons */
        .st-emotion-cache-16idsys, .stInfoIcon, [data-testid="stInfoIcon"], .e1nzilvr5, .css-1gkcr5f, [data-testid="info-icon"] {
            display: none !important;
        }
        
        /* No border or icon for messages */
        .stMessage {
            border: none !important;
            background-color: #F0F2F6 !important;
            padding: 10px 20px !important;
        }
        
        .stMessage > div:first-child {
            display: none !important;
        }
        
        /* Button styles */
        .feature-button {
            display: inline-block;
            padding: 12px 24px;
            background-color: #611e9e;
            color: white;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            border-radius: 8px;
            margin: 10px 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: none;
            font-weight: bold;
            width: 100%;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .feature-button:hover {
            background-color: #4a1984;
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        }
        
        /* Card styles */
        .disease-card {
            background-color: white;
            border-radius: 10px;
            padding: 15px;
            margin: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: all 0.3s ease;
            height: 100%;
        }
        
        .disease-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }
        
        .disease-card h3 {
            color: #611e9e;
            margin-bottom: 8px;
        }
        
        .disease-card p {
            color: #666;
            font-size: 14px;
        }
        
        /* Feature box styles */
        .feature-box {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        
        .feature-box:hover {
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .feature-box h3 {
            color: #611e9e;
            border-bottom: 2px solid #611e9e;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        
        .feature-box p {
            font-size: 15px;
            line-height: 1.6;
            color: #444;
        }
        
        /* Grid container */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 20px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .grid-container {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 480px) {
            .grid-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """
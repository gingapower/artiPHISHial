import React from 'react';
import ReactDOM from 'react-dom';

function MyInput() {
    return ( <
        input type = "text"
        name = "link"
        placeholder = "Link to Website/Login Page" / >
    );
}

function MyButton(props) {
    return ( <
        button onClick = { props.onClick } > { props.text } <
        /button>
    );
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            input: ''
        };
    }

    handleChange = (event) => {
        this.setState({
            input: event.target.value
        });
    }

    handleScrapeClick = () => {
        console.log('Scrape button clicked!');
        console.log('Input:', this.state.input);
    }

    handleAIGeneratedClick = () => {
        console.log('AI Generated button clicked!');
        console.log('Input:', this.state.input);
    }

    render() {
        return ( <
            div class = "app-container" >
            <
            h1 > Generate Your Phishing Page < /h1> <
            MyInput value = { this.state.input }
            onChange = { this.handleChange }
            /> <
            MyButton text = "Scrape"
            onClick = { this.handleScrapeClick }
            /> <
            MyButton text = "AI Generated"
            onClick = { this.handleAIGeneratedClick }
            /> <
            /div>
        );
    }
}

ReactDOM.render( < App / > , document.getElementById('root'));
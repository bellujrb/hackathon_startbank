import React, { useState } from 'react';
import './Jarvis.scss';
import Chat from './plus/Chat';

const Jarvis = ({ onChatInteraction }) => {
    const [messages, setMessages] = useState([
        { text: "No que posso te ajudar hoje, Arthur?", fromUser: false },
        { type: 'button', text: "Ver templates de pagamentos disponíveis no JARVIS", fromUser: false }
    ]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSendMessage = () => {
        if (input.trim()) {
            setMessages([...messages, { text: input, fromUser: true }]);
            setInput('');
            setIsLoading(true);

            setTimeout(() => {
                setMessages((prevMessages) => [
                    ...prevMessages,
                    { text: "Em que mais posso te ajudar hoje?", fromUser: false },
                ]);
                setIsLoading(false);
            }, 2000);

            onChatInteraction(); 
        }
    };

    const handleAutoMessage = () => {
        const autoMessage = "Quero um fluxograma de pagamentos";
        setMessages([...messages, { text: autoMessage, fromUser: true }]);
        setIsLoading(true);

        setTimeout(() => {
            setMessages((prevMessages) => [
                ...prevMessages,
                { text: "Aqui está o seu fluxograma de pagamentos.", fromUser: false },
            ]);
            setIsLoading(false);
        }, 2000);

        onChatInteraction(); 
    };

    return (
        <div className="chatbot-container open">
            <div className="chatbot-content">
                <div className="chatbot-header">
                    <div className="header-info">
                        <img src="public/chat.png" alt="Jarvis Logo" className="header-logo" />
                        <div className='jarvis'>
                            <span className="header-title">Jarvis</span>
                            <span className="header-status">Sempre à disposição</span>
                        </div>
                    </div>
                </div>
                <div className="chatbot-body">
                    <Chat 
                        messages={messages} 
                        input={input} 
                        onSendMessage={handleSendMessage} 
                        setInput={setInput} 
                        isLoading={isLoading} 
                        handleAutoMessage={handleAutoMessage} 
                    />
                </div>
            </div>
        </div>
    );
};

export default Jarvis;

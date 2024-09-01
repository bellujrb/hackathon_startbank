import React from 'react';

const TemplateSelection = () => {
    const handleTemplateClick = (templateName) => {
        // Aqui você pode adicionar uma ação quando o usuário clica em um template, 
        // como exibir uma mensagem ou atualizar algum estado.
        console.log(`Template selecionado: ${templateName}`);
    };

    return (
        <div className="template-selection">
            <h3>Escolha um template:</h3>
            <button className="template-btn" onClick={() => handleTemplateClick('Template 1')}>
                Template 1
            </button>
            <button className="template-btn" onClick={() => handleTemplateClick('Template 2')}>
                Template 2
            </button>
            <button className="template-btn" onClick={() => handleTemplateClick('Template 3')}>
                Template 3
            </button>
        </div>
    );
};

export default TemplateSelection;

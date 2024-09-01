const position = { x: 0, y: 0 };

const nodes = [
    {
        id: "1",
        type: "source",
        data: {
            title: "Acionador",
            description: "API Ecommerce, Compra passagem aerea",
            stats: {
                started: 0,
            },
        },
        position,
    },
    {
        id: "2",
        type: "invoce",
        data: {
            title: "Cobrança",
            description: "Geração QR Code dinamico",
            stats: {
                running: 18,
                error: 1,
            },
        },
        position
    },
    {
        id: "3",
        type: "centerpricepayment",
        data: {
            title: "Split de pagamento",
            description: "Split do valor da cobraça percentual ou estático",
            stats: {
                running: 17,
            },
        },
        position: { x: 250, y: 200 },
    },
    {
        id: "4",
        type: "centerprice",
        data: {
            title: "Centro de Custo",
            description: "Definição de Centro de Custo",
            stats: {
                running: 3,
            },
        },
        position: { x: 100, y: 300 },
    },
    {
        id: "5",
        type: "end",
        data: {
            title: "PIX ou TED",
            description: "Transação financeira PIX para outra conta",
            stats: {
                running: 2,
            },
        },
        position
    },
    {
        id: "6",
        type: "centerprice",
        data: {
            title: "Integração",
            description: "Integração de plataformas como ERP, omie e outras ",
            stats: {
                running: 2,
            },
        },
        position
    },
    {
        id: "7",
        type: "end",
        data: {
            title: "Fim do processo",
            description: "",
            stats: {
                running: 2,
            },
        },
        position
    },
];

const edges = [
    {
        id: "e1-2",
        source: "1",
        target: "2",
        type: "condition",
    },
    {
        id: "e2-3",
        source: "2",
        target: "3",
        type: "condition",
    },
    {
        id: "e3-4",
        source: "3",
        target: "4",
        type: "condition",
        data: {
            title: "Default condition",
            disabled: true,
        },
    },
    {
        id: "e3-5",
        source: "3",
        target: "5",
        type: "condition",
        data: {
            title: "Editable branch",
        },
    },
    {
        id: "e3-6",
        source: "4",
        target: "6",
        type: "condition",
    },
    {
        id: "e4-7",
        source: "6",
        target: "7",
        type: "condition",
        data: {
            title: "Editable branch",
        },
    },
];

export const initialElements = [...nodes, ...edges];

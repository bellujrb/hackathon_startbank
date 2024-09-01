import React, { useState } from 'react';

const centerpriceReceiverForm = () => {
    const [name, setName] = useState('');
    const [taxId, setTaxId] = useState('');
    const [bankCode, setBankCode] = useState('');
    const [branchCode, setBranchCode] = useState('');
    const [accountNumber, setAccountNumber] = useState('');
    const [accountType, setAccountType] = useState('');
    const [receiver, setReceiver] = useState(null);
    const [error, setError] = useState(null);

    const createcenterpriceReceiver = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8080/centerprice-receiver', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: name,
                    tax_id: taxId,
                    bank_code: bankCode,
                    branch_code: branchCode,
                    account_number: accountNumber,
                    account_type: accountType
                })
            });

            if (!response.ok) {
                throw new Error('Erro ao criar o centerpriceReceiver');
            }

            const data = await response.json();
            setReceiver(data);
            setError(null);
        } catch (error) {
            console.error('Erro:', error);
            setError(error.message);
            setReceiver(null);
        }
    };

    return (
        <div>
            <h1>Criar centerpriceReceiver</h1>
            <div>
                <label>
                    Nome:
                    <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                </label>
            </div>
            <div>
                <label>
                    CPF/CNPJ:
                    <input type="text" value={taxId} onChange={(e) => setTaxId(e.target.value)} />
                </label>
            </div>
            <div>
                <label>
                    Código do Banco:
                    <input type="text" value={bankCode} onChange={(e) => setBankCode(e.target.value)} />
                </label>
            </div>
            <div>
                <label>
                    Agência:
                    <input type="text" value={branchCode} onChange={(e) => setBranchCode(e.target.value)} />
                </label>
            </div>
            <div>
                <label>
                    Número da Conta:
                    <input type="text" value={accountNumber} onChange={(e) => setAccountNumber(e.target.value)} />
                </label>
            </div>
            <div>
                <label>
                    Tipo de Conta:
                    <input type="text" value={accountType} onChange={(e) => setAccountType(e.target.value)} />
                </label>
            </div>
            <button onClick={createcenterpriceReceiver}>Criar centerpriceReceiver</button>

            {error && <p style={{ color: 'red' }}>Erro: {error}</p>}

            {receiver && (
                <div>
                    <h2>centerpriceReceiver Criado</h2>
                    <p>ID: {receiver.id}</p>
                    <p>Nome: {receiver.name}</p>
                    <p>CPF/CNPJ: {receiver.tax_id}</p>
                    <p>Código do Banco: {receiver.bank_code}</p>
                    <p>Agência: {receiver.branch_code}</p>
                    <p>Número da Conta: {receiver.account_number}</p>
                    <p>Tipo de Conta: {receiver.account_type}</p>
                </div>
            )}
        </div>
    );
};

export default centerpriceReceiverForm;

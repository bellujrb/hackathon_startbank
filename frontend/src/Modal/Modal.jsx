import React from "react";
import "./Modal.scss"; // Crie esse arquivo CSS para estilizar o modal

const Modal = ({ show, handleClose, children }) => {
    if (!show) {
        return null;
    }

    return (
        <div className="modal-backdrop">
            <div className="modal-content">
                <button className="modal-close" onClick={handleClose}>
                    &times;
                </button>
                {children}
            </div>
        </div>
    );
};

export default Modal;

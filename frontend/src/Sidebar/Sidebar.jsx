// =================================================================================================
import React from "react";

const Sidebar = ({ onAddNodeCallback }) => {
    const onDragStart = (event, nodeType) => {
        event.dataTransfer.setData("nodeType", nodeType); 
    };
    return (
        <div className="sidebar">
            <h5>Arraste os elementos daqui!</h5>
            <div
                className="SidebarItem"
                draggable
                onDragStart={(event) => onDragStart(event, "invoce")}
                key="invoce"
            >
                Cobrança
            </div>
            <div
                className="SidebarItem"
                draggable
                onDragStart={(event) => onDragStart(event, "centerprice")}
                key="centerprice"
            >
                Centro de Custo
            </div>
            <div
                className="SidebarItem"
                draggable
                onDragStart={(event) => onDragStart(event, "centerpricepayment")}
                key="centerpricepayment"
            >
                Splint de Pagamento
            </div>
            <div
                className="SidebarItem"
                draggable
                onDragStart={(event) => onDragStart(event, "end")}
                key="end"
            >
                End
            </div>
        </div>
    );
};

export default Sidebar;

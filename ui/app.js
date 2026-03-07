document.addEventListener('DOMContentLoaded', () => {
    console.log("OpenClaw UI Initialized");
    initKnowledgeGraph();
    initModelControls();
});

function initModelControls() {
    const loadBtn = document.getElementById('load-model-btn');
    const modelSelect = document.getElementById('model-select');
    const statusLight = document.getElementById('model-status-light');
    const modelNameDisplay = document.getElementById('current-model-name');
    const statusDesc = document.querySelector('#model-provider-card .stat-desc');

    loadBtn.addEventListener('click', () => {
        const selectedModel = modelSelect.options[modelSelect.selectedIndex].text;
        
        // Start Loading
        loadBtn.disabled = true;
        statusLight.className = 'status-light loading';
        modelNameDisplay.innerHTML = `<span class="status-light loading"></span>Loading...`;
        statusDesc.textContent = `Initializing parameters for ${selectedModel}...`;

        // Simulate model load time
        setTimeout(() => {
            loadBtn.disabled = false;
            statusLight.className = 'status-light ready';
            modelNameDisplay.innerHTML = `<span class="status-light ready"></span>${selectedModel}`;
            statusDesc.textContent = `Engine: Pulse-D. Model ${selectedModel} is active and ready.`;
        }, 1500);
    });
}

function initKnowledgeGraph() {
    const svg = document.getElementById('graph-svg');
    const nodes = [
        { id: 'OpenClaw', x: 400, y: 200, label: 'Core Engine' },
        { id: 'Moltbook', x: 200, y: 100, label: 'Network' },
        { id: 'ClawdLab', x: 600, y: 100, label: 'Governance' },
        { id: 'Calculus', x: 300, y: 300, label: 'Science Tool' },
        { id: 'Integration', x: 500, y: 300, label: 'Research' }
    ];

    const links = [
        { source: nodes[0], target: nodes[1] },
        { source: nodes[0], target: nodes[2] },
        { source: nodes[0], target: nodes[3] },
        { source: nodes[0], target: nodes[4] },
        { source: nodes[1], target: nodes[4] },
        { source: nodes[2], target: nodes[3] }
    ];

    // Draw links
    links.forEach(link => {
        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("class", "link");
        line.setAttribute("x1", link.source.x);
        line.setAttribute("y1", link.source.y);
        line.setAttribute("x2", link.target.x);
        line.setAttribute("y2", link.target.y);
        if (svg) svg.appendChild(line);
    });

    // Draw nodes
    nodes.forEach(node => {
        const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("class", "node");
        circle.setAttribute("cx", node.x);
        circle.setAttribute("cy", node.y);
        circle.setAttribute("r", 6);

        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("class", "node-label");
        text.setAttribute("x", node.x + 10);
        text.setAttribute("y", node.y + 4);
        text.textContent = node.label;

        g.appendChild(circle);
        g.appendChild(text);
        if (svg) svg.appendChild(g);
    });
}

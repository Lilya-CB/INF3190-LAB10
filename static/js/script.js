function trierNomAZ() {
    console.log("Dans trierNomAZ()");
    // Récupérer la table
    var table = document.getElementById("table-resultat");

    // Récupérer toutes les lignes sauf la première (entête)
    var rows = Array.from(table.getElementsByTagName("tr")).slice(1);

    // Trier les lignes en fonction du premier élément (nom)
    rows.sort(function(a, b) {
        var nomA = a.getElementsByTagName("td")[0].textContent.trim().toUpperCase();
        var nomB = b.getElementsByTagName("td")[0].textContent.trim().toUpperCase();
        if (nomA < nomB) {
            return -1;
        }
        if (nomA > nomB) {
            return 1;
        }
        return 0;
    });

    // Remplacer le contenu de la table par les lignes triées
    for (var i = 0; i < rows.length; i++) {
        table.appendChild(rows[i]);
    }

    return false; // Pour éviter le rechargement de la page
}
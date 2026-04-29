// Compte le nombre d'articles et affiche le résultat
function compterArticles() {
    var articles = document.querySelectorAll(".article");
    var compteur = document.getElementById("compteur");
    compteur.textContent = articles.length + " article(s) publié(s)";
}

// Demande confirmation avant de supprimer un article
function confirmerSuppression(lien) {
    var ok = confirm("Tu veux vraiment supprimer cet article ?");
    if (ok) {
        window.location = lien; // redirige vers /supprimer/...
    }
}
// On lance au chargement de la page
compterArticles();

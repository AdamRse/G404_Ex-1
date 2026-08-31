*Répondez aux questions suivantes :*

## Question 1 : Afficher pour chaque inscription en cours le nombre de jours écoulés depuis la date d'inscription.
```sql
SELECT 
    CURRENT_DATE - date_inscription AS jours_ecoules
FROM inscriptions
WHERE statut = 'en cours';
```

## Question 2 : Lister les ateliers prévus dans le futur.
```sql
SELECT *
FROM ateliers
WHERE NOW() < date_atelier;
```

## Question 3 : Afficher l'âge de chaque apprenant en années (indice : utiliser la fonction AGE()).
```sql
SELECT 
    prenom,
    nom,
    date_naissance,
    EXTRACT(YEAR FROM AGE(date_naissance)) AS age_annees
FROM apprenants;
```

## Question 4 : Combien d'apprenants ont leur anniversaire chaque mois ?
```sql
SELECT 
    EXTRACT(MONTH FROM date_naissance) AS mois,
    COUNT(*) AS nb_anniversaires
FROM apprenants
GROUP BY EXTRACT(MONTH FROM date_naissance)
ORDER BY mois;
```

## Question 5 : Afficher la date d'adhésion de chaque apprenant au format jour, mois, année.
```sql
SELECT 
    prenom,
    nom,
    TO_CHAR(date_adhesion, 'DD-MM-YYYY') AS date_adhesion_formattee
FROM apprenants;
```

## Question 6 : Afficher chaque atelier avec sa date au format JJ/MM/AAAA et son heure au format HH:MM sur 24h.
```sql
SELECT 
    titre,
    TO_CHAR(date_atelier, 'DD/MM/YYYY') AS date_formattee,
    TO_CHAR(date_atelier, 'HH24:MI') AS heure_formattee,
    duree_heures,
    ville
FROM ateliers;
```

## Question 7 : Calculer le prix par semaine de chaque formation avec 2 décimales (sans utiliser ROUND).
```sql
SELECT 
    titre,
    prix,
    duree_semaines,
    CAST(prix / duree_semaines AS NUMERIC(8,2)) AS prix_par_semaine
FROM formations;
```

## Question 8 : Afficher chaque apprenant sous la forme : 'prenom NOM : inscrit(e) en annee'.
```sql
SELECT 
    prenom || ' ' || UPPER(nom) || ' : inscrit(e) en ' || EXTRACT(YEAR FROM date_adhesion) AS presentation
FROM apprenants;
```

## Question 9 : Pour chaque apprenant, afficher son nombre d'inscriptions à des formations.
```sql
SELECT 
    a.prenom,
    a.nom,
    (
        SELECT COUNT(*)
        FROM inscriptions i
        WHERE i.apprenant_id = a.id
    ) AS nb_inscriptions
FROM apprenants a;
```

## Question 10 : Afficher la note moyenne obtenue dans chaque formation (via une sous-requête).
```sql
SELECT 
    f.titre,
    (
        SELECT AVG(note)
        FROM evaluations e
        WHERE e.formation_id = f.id
    ) AS note_moyenne
FROM formations f;
```

## Question 11 : Afficher les apprenants domiciliés dans une ville qui héberge au moins une entreprise partenaire.
```sql
SELECT *
FROM apprenants
WHERE ville IN (SELECT ville FROM entreprises);
```

## Question 12 : Afficher les apprenants inscrits à la formation Cybersécurité (utiliser IN).
```sql
SELECT *
FROM apprenants
WHERE id IN (
    SELECT apprenant_id
    FROM inscriptions
    WHERE formation_id IN (
        SELECT id
        FROM formations
        WHERE titre = 'Cybersécurité'
    )
);
```

## Question 13 : Quels apprenants sont (ou ont été) inscrits à une formation coûtant plus de 9000 euros ?
```sql
SELECT DISTINCT a.*
FROM apprenants a
JOIN inscriptions i ON a.id = i.apprenant_id
JOIN formations f ON i.formation_id = f.id
WHERE f.prix > 9000;
```

## Question 14 : Afficher les apprenants ayant eu au moins une évaluation.
```sql
SELECT *
FROM apprenants a
WHERE EXISTS (
    SELECT *
    FROM evaluations e
    WHERE e.apprenant_id = a.id
);
```

## Question 15 : Afficher les ateliers qui n'ont enregistré aucune participation. Trouver deux solutions.
```sql
-- Solution 1 : avec NOT EXISTS
SELECT *
FROM ateliers a
WHERE NOT EXISTS (
    SELECT *
    FROM participations p
    WHERE p.atelier_id = a.id
);

-- Solution 2 : avec LEFT JOIN / IS NULL
SELECT a.*
FROM ateliers a
LEFT JOIN participations p ON a.id = p.atelier_id
WHERE p.atelier_id IS NULL;
```

## Question 16 : Lister (sans doublon) les villes où il y a au moins un apprenant, un formateur, un atelier ou une entreprise partenaire.
```sql
SELECT ville FROM apprenants
UNION
SELECT ville FROM formateurs
UNION
SELECT ville FROM ateliers
UNION
SELECT ville FROM entreprises;
```

## Question 17 : Afficher les villes qui hébergent à la fois un formateur et un apprenant.
```sql
SELECT ville FROM formateurs
INTERSECT
SELECT ville FROM apprenants;
```

## Question 18 : Pour chaque inscription, afficher le montant payé en remplaçant NULL par 0, puis calculer le reste à payer.
```sql
SELECT 
    i.id AS inscription_id,
    a.prenom,
    a.nom,
    f.titre AS formation,
    COALESCE(i.montant_paye, 0) AS montant_paye,
    f.prix - COALESCE(i.montant_paye, 0) AS reste_a_payer
FROM inscriptions i
JOIN apprenants a ON i.apprenant_id = a.id
JOIN formations f ON i.formation_id = f.id;
```

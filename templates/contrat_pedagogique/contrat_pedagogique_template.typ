#import "../erasmus_plus_utils/erasmus_plus_template_utils.typ" : * 

#let contrat_pedagogique(
  name : "",
  firstname : "",
  address: "",
  email: "",
  phone: "",
  activity_type: "",
  start_date: "",
  end_date: "",
  country_town: "",
  guardians: (),
  acquis_list: (),
  activities: (),
  tutorings: (),
  project_code: "",
  sending_organisation_name: "",
  sending_organisation_address: "",
  sending_organisation_email: "",
  sending_organisation_phone: "",
  hosting_organisation_name: "",
  hosting_organisation_address: "",
  hosting_organisation_email: "",
  hosting_organisation_phone: "",
  qualification: "",
  school_year: "",
  european_qualification_framework: "",
  staff_qualification: "",
  staff_school_year: "",
  staff_european_qualification_framework: "",
  hosting_responsables: (
    (name: "",
    firstname: "",
    email: "",
    phone: "",
    responsabilities: ""),
  ),
  sending_responsables: (
    (name: "",
    firstname: "",
    email: "",
    phone: "",
    responsabilities: ""),
  ),
  companions : (
    (name: "",
    firstname: "",
    email: "",
    phone: "",
    responsabilities: ""),
  ),
  ..superfluous_arguments
 ) = [

#show: doc => erasmus_plus_layout(
  title:[CONTRAT PÉDAGOGIQUE ERASMUS+], 
  translation: "ERASMUS+ learning agreement",
  doc
)

= Objectifs du contrat pédagogique

#chap[
    
    Ce contrat pédagogique définit les conditions et les acquis d’apprentissage attendus d’une mobilité à des fins d’apprentissage organisée dans le cadre du programme Erasmus+. Les parties prenantes à ce contrat doivent se conformer aux règles et aux standards de qualité du programme.

    _#englishStyling[This learning agreement defines the conditions and learning outcomes expected from a learning mobility organised as part of the Erasmus+ programme. The parties to this contract must comply with the programme’s rules and quality standards]_

]

= Information sur la mobilité à des fins d’apprentissage
#chap[
    
  #form((
    "Secteur": "Enseignement et formation professionnels",
    "Type d’activité":activity_type,
    "Pays, Ville":country_town,
    "Date de début":start_date,
    "Date de fin":end_date, 
  ))

]


= Parties prenantes au contrat pédagogique
#chap[
    
    Le contrat pédagogique est conclu entre le participant à la mobilité à des fins d’apprentissage, l’organisme d’envoi et l’organisme d’accueil. 
    
    _#englishStyling[The learning agreement is concluded between the participant in the learning mobility, the sending organisation and the hosting organisation.]_

]

= Participant à la mobilité à des fins d’apprentissage
#chap[

=== Participant
  #form((
      "Nom":name,
      "Prénom":firstname,
      "Adresse":address,
      "Adresse mail":email,
      "Téléphone":phone,
    )
  )
  
#let index = 1
#for guardian in guardians {
  
  let displayed_index = if guardians.len() == 1 {""} else {index} 
  [=== Tuteur légal #displayed_index]
  form((
      "Nom":guardian.name,
      "Prénom" :guardian.firstname,
      "Adresse mail":guardian.email,
      "Téléphone":guardian.phone
    ))
  index = index + 1

}
]

== Organisme d’envoi
#chap[

  #form((
        "Nom de l'organisme":sending_organisation_name,
        "Adresse":sending_organisation_address,
        "Adresse mail":sending_organisation_email,
        "Téléphone":sending_organisation_phone
      ))
]

== Organisme d’accueil
#chap[
  
  #form((
        "Nom de l'organisme":hosting_organisation_name,
        "Adresse":hosting_organisation_address,
        "Adresse mail":hosting_organisation_email,
        "Téléphone":hosting_organisation_phone
      )
    )
]

= Contexte d’apprentissage
#chap[

  Au sein de l’organisme d’envoi, le participant est actuellement inscrit à :
  
  #englishStyling[At the sending organisation, the participant is currently enrolled in :]

  === Apprenant
  #form((
    "Titre qualification / profession": qualification,
    "Année scolaire": school_year,
    "Niveau dans le Cadre Européen des Certifications": european_qualification_framework
  ),wide_title: true)

  Au sein de l’organisme d’envoi, le participant occupe actuellement la fonction de :
  
  #englishStyling[At the sending organisation, the participant is currently working in the following capacity :]

  === Personnel
  #form((
    "Titre qualification / profession":staff_qualification,
    "Année scolaire":staff_school_year,
    "Niveau dans le Cadre Européen des Certifications":staff_european_qualification_framework
  ),wide_title: true)

]
= Acquis d’apprentissage
#chap[

  Les parties ont convenu que les acquis d’apprentissage suivants devraient être atteints au cours de la mobilité à des fins d’apprentissage :
  
  _#englishStyling[The parties have agreed that the following learning outcomes should be achieved during the learning mobility :]_

  #for acquis in acquis_list {
    [- #acquis]
  }

]
  
= Programme d’apprentissage et tâches

#chap[
  Pour atteindre les acquis d’apprentissage convenus, le participant réalisera les activités et tâches suivantes au cours de son activité de mobilité.
  
  _#englishStyling[To achieve the agreed learning outcomes, the participant will complete the following activities and tasks during their mobility activity.]_
    
  #for activity in activities {
    [- #activity]
  }
]

= Suivi et tutorat du participant durant l’activité

== Personnes responsables au sein de l’organisme d’accueil

#chap[

  La (les) personne(s) suivante(s) de l’organisme d’accueil est (sont) chargée(s) de présenter au participant ses activités et ses tâches au sein de l’organisme d’accueil, de lui fournir un soutien pratique, de suivre ses progrès d’apprentissage, de l’aider à atteindre les acquis d’apprentissage attendus et de l’aider à s’intégrer dans lesroutines quotidiennes et le contexte social de l’organisme d’accueil. 
  
  _#englishStyling[The following person(s) at the hosting organisation are tasked with introducing the participant to their activities and tasks at the hosting organisation, providing practical support, monitoring their learning progress, supporting them to achieve the expected learning outcomes, and helping them to integrate into the daily routines and the social context at the hosting organisation.]_

  #for person in hosting_responsables {
    form((
      "Nom": person.name,
      "Prénom":person.firstname,
      "Adresse mail":person.email,
      "Téléphone":person.phone,
      "Responsabilités":person.responsabilities,
    ))
  }

]


== Personnes responsables au sein de l’organisme d’envoi

#chap[
  La (les) personne(s) suivante(s) de l’organisme d’envoi est (sont) chargée(s) de suivre les progrès des participants et de fournir un contenu ou un soutien pratique de la part de l’organisme d’envoi.
  
  #englishStyling[The following person(s) at the sending organisation are tasked with following the participants' progress and providing content or practical support from the side of the sending organisation.]

  #for person in sending_responsables {
    form((
      "Nom": person.name,
      "Prénom":person.firstname,
      "Adresse mail":person.email,
      "Téléphone":person.phone,
      "Responsabilités":person.responsabilities
    )
  )
  }
]

= Accompagnateurs

#chap[

  La ou les personnes suivantes accompagneront le participant pendant sa période de mobilité.
  
  #englishStyling[The following person(s) will accompany the participant during their mobility period]

  #for person in companions {
    form((
      "Nom": person.name,
      "Prénom":person.firstname,
      "Adresse mail":person.email,
      "Téléphone":person.phone,
      "Responsabilités":person.responsabilities,
    )
  )
  }
]

== Modalités de suivi et de tutorat

#chap[

    #for tutoring in tutorings {
      [- #tutoring]
    }
  
]

= Évaluation des acquis d’apprentissage

= Reconnaissance des acquis d’apprentissage

= Réintégration dans l’organisme d’envoi

= Disposition supplémentaires

= Signatures

#chap[
  Les signataires confirment qu’ils ont compris et approuvent le contenu de cet accord.
  
  #englishStyling[The signatories confirm that they understood and approve the content of this agreement.]

  #let signatures_dict = (
    "Organisme d’envoi": sending_organisation_name,
    "Organisme d’accueil": sending_organisation_name
  )
  
  #let index = 1
  #for guardian in guardians {
     signatures_dict.insert("Tuteur légal", guardian.name + " " + guardian.firstname)
    index = index + 1
  }
  #signatures_dict.insert("Participant", name + " " + firstname )

  #signatures(signatures_dict)
]

]

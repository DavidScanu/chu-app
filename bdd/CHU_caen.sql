-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : db
-- Généré le : lun. 19 déc. 2022 à 20:27
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `CHU_caen`
--

-- --------------------------------------------------------

--
-- Structure de la table `archives`
--

CREATE TABLE `archives` (
  `identifiant_resident` varchar(200) NOT NULL,
  `date_entree` date DEFAULT NULL,
  `date_sortie` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `archives`
--

INSERT INTO `archives` (`identifiant_resident`, `date_entree`, `date_sortie`) VALUES
('biduloumargaux19900510', '2022-12-02', '2022-12-14'),
('creancearnaud19830615a+', '2022-12-14', '2022-11-24'),
('dupontmichel19851220', '2022-12-01', '2022-12-29'),
('haltunecyril19940323', '2022-09-20', NULL),
('melenchonjean-luc19510819', '2022-12-19', '2022-12-22'),
('scanudavid19831211b-', '2022-12-01', '2022-12-23');

-- --------------------------------------------------------

--
-- Structure de la table `patients`
--

CREATE TABLE `patients` (
  `identifiant_patient` varchar(200) NOT NULL,
  `nom` varchar(200) DEFAULT NULL,
  `prenom` varchar(200) DEFAULT NULL,
  `date_naissance` date NOT NULL,
  `groupe_sanguin` varchar(3) DEFAULT NULL,
  `is_in_hospital` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `patients`
--

INSERT INTO `patients` (`identifiant_patient`, `nom`, `prenom`, `date_naissance`, `groupe_sanguin`, `is_in_hospital`) VALUES
('baltranolivier19900130ab+', 'Baltran', 'Olivier', '1990-01-30', 'AB+', 0),
('chambersmax20141026a+', 'Chambers', 'Max', '2014-10-26', 'A+', 0),
('creancearnaud19830615a+', 'Creance', 'Arnaud', '1983-06-15', 'A+', 0),
('einsteinalbert18790314a+', 'Einstein', 'Albert', '1879-03-14', 'A+', 0),
('engebretsensanne19670523b+', 'Engebretsen', 'Sanne', '1967-05-23', 'B+', 0),
('evanspeyton19780201a-', 'Evans', 'Peyton', '1978-02-01', 'A-', 0),
('helsetøystein20090609b+', 'Helset', 'Øystein', '2009-06-09', 'B+', 0),
('moradihedda20211224a-', 'Moradi', 'Hedda', '2021-12-24', 'A-', 0),
('prinaudalbert19900123a+', 'Prinaud', 'Albert', '1990-01-23', 'A+', 0),
('sullivanannette19560306b+', 'Sullivan', 'Annette', '1956-03-06', 'B+', 0);

-- --------------------------------------------------------

--
-- Structure de la table `rh`
--

CREATE TABLE `rh` (
  `identifiant_rh` varchar(200) NOT NULL,
  `nom` varchar(200) DEFAULT NULL,
  `prenom` varchar(200) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `salaire` int DEFAULT NULL,
  `working_at_hospital` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `rh`
--

INSERT INTO `rh` (`identifiant_rh`, `nom`, `prenom`, `date_naissance`, `salaire`, `working_at_hospital`) VALUES
('biduloumargaux19900510', 'Bidulou', 'Margaux', '1990-05-10', 91835, 0),
('brarjeanne19790413', 'Brar', 'Jeanne', '1979-04-13', 25507, 0),
('dupontmichel19851220', 'Dupont', 'Michel', '1985-12-20', 30000, 0),
('haltunecyril19940323', 'Haltune', 'Cyril', '1994-03-23', 118129, 1),
('harmslucie19630208', 'Harms', 'Lucie', '1963-02-08', 56978, 0),
('hawkanna1992-12-20', 'Hawk', 'Anna', '1992-12-20', 30000, 0),
('melenchonjean-luc19510819', 'Melenchon', 'Jean-Luc', '1951-08-19', 155180, 0),
('scanudavid19831211', 'Scanu', 'David', '1983-12-11', 151595, 0),
('tveitamadeus20060522', 'Tveit', 'Amadeus', '2006-05-22', 39185, 0),
('wichmannlore19790619', 'Wichmann', 'Lore', '1979-06-19', 46761, 0);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `archives`
--
ALTER TABLE `archives`
  ADD PRIMARY KEY (`identifiant_resident`);

--
-- Index pour la table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`identifiant_patient`);

--
-- Index pour la table `rh`
--
ALTER TABLE `rh`
  ADD PRIMARY KEY (`identifiant_rh`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

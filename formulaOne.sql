create table Seasons(
    num_of_races int not null CHECK (num_of_races between 7 and 23),
    team_ID int not null CHECK (team_ID between 0 and 26),
    year_of_comp int not null check (year_of_comp between 1950 and 2023),
    primary key(year_of_comp),
    foreign key (team_ID) references team(team_ID)
);

create table Team(
    team_Name varchar(32),
    team_ID int not null CHECK (team_ID between 0 and 26),
    team_points int not null CHECK (team_points between 0 and 25000),
    base varchar(24),
    team_chief varchar(32),
    tech_chief varchar(32),
    chassis varchar(24),
    engine varchar(24),
    championship_count int not null CHECK (championship_count between 0 and 20),
    wins int not null CHECK (wins between 0 and 300),
    year_of_comp int not null check (year_of_comp between 1950 and 2023),
    driver_Num int not null CHECK (driver_Num between 1 and 99),
    primary key(team_ID), 
    foreign key (year_of_comp) references Seasons(year_of_comp),
    foreign key (driver_Num) references Driver(driver_Num)
);
 
create table Driver(
    driver_Num int not null CHECK (driver_Num between 1 and 99),
    last_Name varchar(24), 
    first_Name varchar(24),
    racing_Country varchar(24),
    birth_Country varchar(24),
    dob varchar(64),
    highest_grid int not null CHECK (highest_grid between 1 and 50), 
    highest_finish int not null CHECK (highest_finish between 1 and 50),
    podiums int not null CHECK (podiums between 0 and 300),
    season_points int not null CHECK (season_points between 0 and 5000),
    championships int not null CHECK (championships between 0 and 10),
    team_ID int not null check (team_ID between 0 and 26),
    primary key(driver_Num),
    foreign key (team_ID) references Team(team_ID)
);
 
 create table driverStandings(
    driver_standing_id int not null CHECK (driver_standing_id between 1 and 51),
    year int not null check (year between 1950 and 2023),
    place int not null CHECK (place between 1 and 50),
    total_points int not null CHECK (total_points between 0 and 5000),
    driver_Num int not null CHECK (driver_Num between 1 and 99),
    primary key (driver_standing_id),
    foreign key(driver_Num) references Driver(driver_Num)
);
 
 create table teamStandings(
    team_standing_ID int not null CHECK (team_standing_ID between 1 and 26),
    ranking int not null CHECK (ranking between 1 and 26),
    team_ID int not null CHECK(team_ID between 0 and 26),
    year_of_comp int not null check (year_of_comp between 1950 and 2023),
    primary key(team_standing_ID),
    foreign key(team_ID) references Team(team_ID),
    foreign key (year_of_comp) references Seasons(year_of_comp)
);

create table Sponsors(
    sponsor_ID int not null CHECK (sponsor_ID between 1 and 275),
    company_name varchar(32),
    sponsor_website varchar(64),
    team_ID int not null CHECK(team_ID between 0 and 26),
    primary key(sponsor_ID),
    foreign key(team_ID) references Team(team_ID)
);

create table Course(
    location varchar(24),
    record_lap double not null check (record_lap between 90 and 120),
    num_of_laps int not null CHECK (num_of_laps between 160 and 500),
    total_length int not null CHECK (total_length between 100 and 300),
    driver_Num int not null CHECK (driver_Num between 1 and 99),
    event_date varchar(64),
    primary key(location),
    foreign key (driver_Num) references Driver(driver_Num),
    foreign key (event_Date) references raceResults(event_Date)
);

 create table raceResults(
    event_date varchar(64),
    fastest_lap double not null check (fastest_lap between 90 and 120),
    laps int not null CHECK (laps between 44 and 500),
    points_awarded int not null CHECK (points_awarded between 1 and 50), 
    finishing_Place int not null CHECK (finishing_Place between 1 and 50),
    location varchar(24),
    driver_Num int not null CHECK (driver_Num between 1 and 99),
    primary key (event_date), 
    foreign key (driver_Num) references driver(driver_Num),
    foreign key (location) references Course(location)
);
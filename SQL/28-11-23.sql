SELECT * FROM avaliacoes;

//média turma
SELECT avg (nota) FROM avaliacoes WHERE turma = 'A';
SELECT avg (nota) FROM avaliacoes WHERE turma = 'B';
SELECT avg (nota) FROM avaliacoes WHERE turma = 'C';

//média bimestre
SELECT avg (nota) FROM avaliacoes WHERE bimestre = 1;
SELECT avg (nota) FROM avaliacoes WHERE bimestre = 2;
SELECT avg (nota) FROM avaliacoes WHERE bimestre = 3;

//média turma
SELECT max(nota) FROM avaliacoes WHERE turma = 'A';
SELECT max(nota) FROM avaliacoes WHERE turma = 'B';
SELECT max(nota) FROM avaliacoes WHERE turma = 'C';


SELECT turma, count(turma) as quantidadeDeAlunos FROM avaliacoes GROUP by turma;
SELECT bimestre, count(bimestre) as quantidadeDeAlunos FROM avaliacoes GROUP by bimestre;
SELECT id_aluno, nome, count(nota) as QuantidadeDeAvaliações FROM avaliacoes GROUP by id_aluno;

//média de notas de cada turma
SELECT turma, avg(nota) as MédiaDeNotas FROM avaliacoes GROUP by turma;

// quantidade de alunos em cada turma
SELECT turma, count(turma) as QuantidadeDeAlunos FROM avaliacoes GROUP by turma;

// média geral de cada bimestre
SELECT bimestre, avg(nota) as média FROM avaliacoes GROUP by bimestre;

// média de cada bimestre e cada turma
SELECT bimestre, turma, avg(nota) as Média FROM avaliacoes GROUP by bimestre, turma;

//O arquivo é curso
//Faça uma consulta para obter uma tabela com a média final de cada aluno
SELECT id_aluno, nome, turma, avg(nota) as MédiaFinal FROM avaliacoes GROUP by nota;

//Modifique a consulta feita anteriormente para que apenas alunos aprovados (com média >=6) apareçam
SELECT id_aluno, nome, turma, avg(nota) as Aprovado FROM avaliacoes GROUP by nota HAVING avg(nota) >= 6;

//Modifique a consulta feita anteriormente para que apenas alunos reporvados (com média < 6) apareçam
SELECT id_aluno, nome, turma, avg(nota) as Reprovado FROM avaliacoes GROUP by nota HAVING avg(nota) < 6;


//O arquivo é banco
//Faça um select para obter uma tabela com nome, email, número da conta e agência
SELECT cliente.nome, cliente.email, conta.numero, conta.agencia FROM cliente JOIN conta on conta.cliente_id = cliente.id;

//Faça um SELECT para obte uma tabela de transferências com Número da conta de destino e valor
SELECT conta.numero, transferencia.valor FROM conta JOIN transferencia on transferencia.conta_destino_id = conta.id;

//Faça um SELECT para obter uma tabela de transf com numero da conta de origem e valor
SELECT conta.numero, transferencia.valor FROM conta  OIN transferencia on transferencia.conta_origem_id = conta.id;


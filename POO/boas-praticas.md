# Boas Práticas para Usar Git e GitHub

## 1. Escreva mensagens de commit claras e descritivas

Cada commit deve explicar **o que** foi feito e, quando necessário, **por quê**. Prefira mensagens no formato convencional:

```
tipo: descrição curta no imperativo

Exemplos:
feat: adiciona classe Animal com método falar
fix: corrige cálculo de média na função mediana
docs: atualiza README com instruções de uso
```

Evite mensagens vagas como `"ajustes"`, `"correções"` ou `"wip"`.

---

## 2. Organize o trabalho em branches

Nunca desenvolva diretamente na branch `main`. Crie branches específicas para cada funcionalidade, correção ou experimento:

- `feature/nome-da-funcionalidade` — para novas funcionalidades
- `fix/descricao-do-bug` — para correções de bugs
- `docs/atualizacao-documentacao` — para alterações em documentação

Isso mantém a `main` sempre estável e facilita revisões de código.

---

## 3. Faça commits pequenos e frequentes

Prefira commitar mudanças pequenas e coesas, em vez de acumular muitas alterações em um único commit gigante. Commits menores:

- São mais fáceis de revisar
- Facilitam reverter um erro específico com `git revert`
- Tornam o histórico do projeto mais legível

---

## 4. Use Pull Requests para revisão de código

Antes de mesclar qualquer branch na `main`, abra um Pull Request (PR) no GitHub. O PR permite que outros revisem o código, façam comentários e garantam a qualidade antes da integração.

---

## 5. Mantenha o repositório local atualizado

Antes de começar a trabalhar, sempre sincronize com o remoto:

```bash
git pull origin main
```

Isso evita conflitos desnecessários ao integrar seu trabalho com o da equipe.

# Contributing

Suggestions for new papers, corrections, and official implementation links are welcome. [Open an issue](https://github.com/Collab-Gen/Awesome-sparse-attention-for-visual-generation/issues/new/choose) or submit a pull request against `main`.

## Adding a paper

1. Search [data/papers.json](data/papers.json) by title, arXiv ID, or DOI. If a published version supersedes a preprint, update the same record. Keep its existing ID so links and section memberships carry over.
2. Add the title, bibliographic year, and `first_public` date. Use the arXiv v1 submission date or the earliest date you can verify from the paper's public record. Use `YYYY-MM` if you can verify only the month. The tables sort by this date and display the bibliographic year.
3. Give the record an `arxiv:<id>` or `doi:<doi>` identifier. For a paper with neither, use a unique `venue:<slug>` and include its proceedings URL. An optional `url` overrides the default arXiv or DOI link. Add a `code` object with `label` and `url` when an official implementation is available.
4. Add the relevant section tags. One record can appear in several tables. Explain the paper's connection to the [4+1+3 framework](README.md#the-413-framework) in your pull request.
5. Regenerate the README and include both the catalog and the generated diff in your pull request.

```bash
python3 scripts/render_readme.py
python3 scripts/render_readme.py --check
```

The generator uses Python 3.8 or newer and its standard library. Edit the catalog for changes to a generated table. For a paper mentioned in README prose or in an example, use `[Display label][paper:arxiv:2605.22718]` with the record's ID. The generator updates the link definition.

### Section tags

| README area | Tags |
| --- | --- |
| Static sparse attention | `mechanism-structural`, `mechanism-calibrated` |
| Dynamic evidence construction | `mechanism-pooling`, `mechanism-sampling`, `mechanism-clustering`, `mechanism-learned` |
| Applications | `application-image`, `application-video`, `application-long-video`, `application-streaming`, `application-video-editing`, `application-world-models`, `application-3d-4d`, `application-audio-visual` |
| Additional references | `related-training-free`, `related-trainable`, `related-systems` |

The optional `featured` object controls the **Start here** table. It contains the method's short `name` and a brief `note` on what to look for. A paper cited only in prose or in an example can use an empty `sections` array.

## Correcting an entry

Point to the affected record and include a primary source, such as the paper, proceedings page, or authors’ repository. For a classification change, identify the relevant figure, section, or experiment in the paper.

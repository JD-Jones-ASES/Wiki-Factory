---
title: "Sampling Methods and Bias"
type: topic
aliases: ["Random Sampling", "Stratified Sampling", "Cluster Sampling", "Selection Bias", "Survey Bias"]
tags: ["#branch-algebra-2", "#topic-statistics", "#skill-translation", "#skill-multi-step", "#key-topic", "#word-problem-support", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algebra_2", chapter: "11", section: "11.4"}
related:
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/algebra/Scatter_Plots_And_Trend_Lines"
  - "topics/algebra/Histograms_And_Box_Plots"
  - "topics/algebra/Correlation_And_Residuals"
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
problem_type_ids: []
figures: []
summary: "Population vs sample, the five main sampling methods, and how selection bias and response bias can wreck a survey's conclusions."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Sampling Methods and Bias

# Sampling Methods and Bias

Whenever a newspaper reports that "$62\%$ of high schoolers say they want later start times" or a health study claims that "$1$ in $4$ adults don't get enough sleep," somebody had to collect that number. They almost never asked every single person in the group --- that would be impossibly expensive and, for something like "all U.S. teenagers," literally impossible to finish. Instead, they asked a carefully chosen **sample** and used its answer to estimate what the whole **population** would say. The catch is that not every sample tells the truth about its population. Choose badly --- or phrase the question badly --- and your "$62\%$" can be off by fifteen points without you ever noticing.

---

## Population, sample, and the inference leap

The **population** is the entire group you actually want to know about: every student at a high school, every registered voter in a state, every shipment of cereal leaving a factory this month. The **sample** is the much smaller subset you gather data from: the $200$ students you surveyed, the $1{,}000$ voters a pollster called, the $30$ cereal boxes a quality inspector pulled from the belt.

When you compute a statistic from the sample --- an average, a percentage, a proportion --- you use it as an *estimate* of the matching value for the entire population. This jump from "what the sample said" to "what the population is like" is called **generalization** or **statistical inference**. The whole machinery of survey statistics exists to make that leap safer. A well-drawn sample supports a confident generalization. A badly drawn sample supports nothing at all, no matter how large it is.

Two big ideas govern whether a sample supports generalization: *how* the sample was chosen (the **sampling method**) and *whether* something systematic pushed the answers off-target (**bias**).

---

## The five sampling methods

Textbooks and standardized tests center on five ways to draw a sample. The first three are considered **probability-based** and are the gold standard; the last two are considered weak and are usually a red flag.

### Simple random sampling

Every individual in the population has the exact same chance of being picked, and each selection is independent of the others. A classic implementation: number everyone in the population, then use a random-number generator or a hat of numbered slips to pick $n$ of them. Because chance alone decides who ends up in the sample, there is no systematic reason for the sample to over-represent or under-represent any particular slice of the population.

### Stratified random sampling

First divide the population into non-overlapping **strata** --- subgroups you believe may answer differently. Then draw a simple random sample from each stratum, usually in proportion to the stratum's size. For example, to study school satisfaction you might split students by grade level ($9$, $10$, $11$, $12$) and randomly pick, say, $25$ from each grade. This guarantees that every subgroup is represented in the sample at roughly the right proportion, which reduces variability compared to a pure simple random sample of the same size.

### Cluster sampling

Divide the population into many naturally occurring **clusters** (homerooms, apartment buildings, city blocks) and then randomly choose a few *whole* clusters to survey. Everyone inside a chosen cluster is included. Cluster sampling is cheaper than simple random sampling when travel or contact costs matter, because the surveyors don't have to chase individuals scattered all over the map --- they go to a handful of clusters and sweep each one.

### Systematic sampling

Order the population somehow --- alphabetically, by customer number, by arrival time --- and then pick every $k$-th individual after a random start. For example, if the population has $800$ people and you want a sample of size $50$, you pick a random start between $1$ and $16$ and then take every $16$-th name on the list. Systematic sampling is fast and easy, and in most situations it behaves like a simple random sample. The one gotcha: if the ordering has a hidden periodic pattern that lines up with your step $k$, you can accidentally sample only one "type" of person.

### Convenience sampling

Whoever is easiest to reach is whoever you ask. The first $30$ people walking past a particular coffee shop. The students in your own homeroom. Whoever happens to reply to your online post. Convenience sampling is almost never defensible for serious generalization, because the people who are easy to reach are systematically different from the people who are not. Conclusions from a convenience sample apply --- at best --- only to the kind of person who was reachable, not to the whole population.

---

## Two kinds of bias

**Bias** is any systematic tendency of a sample or survey to miss the true population value. It is not random noise. Random noise averages out as your sample gets bigger; bias does not. A biased survey of $10{,}000$ people can still be dead wrong.

Two categories cover most of what students are asked about on tests.

### Selection bias

Selection bias happens when the *method of picking people* favors certain kinds of respondents over others. The sample is built from a slanted pool before anyone has even answered a question. Examples:

- Surveying only people who answer the landline telephone during the workday (who is *home* at $2$ p.m.?).
- Asking about exercise habits by posting a survey link on a fitness subreddit.
- Estimating the typical student workload by polling only honor-roll students.
- Measuring customer satisfaction by handing out feedback cards in the store --- you hear from people who are still shopping there, never from those who gave up and left.

In each case, the sampling frame excludes part of the population with a specific opinion, so the remaining answers tilt in a predictable direction.

### Response bias

Response bias happens when the *answers themselves* are systematically distorted, even if the sampling frame was perfect. Common causes include:

- **Leading or loaded questions.** "Do you support the reasonable proposal to keep our neighborhood safe?" will get a different yes-rate than "Do you support Proposal 4?"
- **Socially desirable answering.** On a sensitive topic --- exercise frequency, honesty, voting behavior --- respondents shade their answers toward what sounds good rather than what is true.
- **Non-response bias.** People who refuse to answer are systematically different from people who reply. If $90\%$ of the people you contacted refused, the $10\%$ who replied are not a random slice.
- **Interviewer effects.** The same question asked by a stern authority figure versus a friendly peer elicits different answers.

Unlike selection bias, response bias can sneak into a beautifully random sample. Even after drawing names out of a hat, a sloppy question wording can still give a wrong answer.

---

## When can you generalize?

A sample supports generalization to a population when two conditions both hold.

1. **The sampling method was probability-based** (simple random, stratified, cluster, or systematic), so every part of the population had some known, non-zero chance of being picked.
2. **The sampling frame matches the population you actually care about.** A random sample of tenth-graders at one high school can tell you about tenth-graders at that school, not about high schoolers nationwide.

If either fails, you should not extrapolate the finding beyond the actual sampled group.

---

## Example 1: Classifying a sampling method

> A middle-school principal wants to survey $60$ students about the cafeteria menu. She sorts the $720$ students on the roster by grade ($6$, $7$, $8$), then from each grade she randomly selects $20$ students. Classify the sampling method.

Determine which category this procedure fits. The population is partitioned into non-overlapping subgroups (grades), each subgroup is a coherent slice the principal expects might answer differently, and a simple random sample is drawn *from each subgroup*. That is the textbook definition of **stratified random sampling**. The sample of $60$ is split $20$-$20$-$20$ across the three grades.

Notice what this is *not*. It is not simple random sampling: if it were, the principal would draw $60$ names from one combined list of $720$, and nothing would guarantee a balanced grade split. It is not cluster sampling, because whole grades are not being selected wholesale --- only a random slice of each grade is. Stratified sampling is a common choice in school surveys because it prevents a lopsided sample (e.g., accidentally drawing $40$ eighth-graders and only $10$ sixth-graders).

---

## Example 2: Identifying the bias source

> A student reporter wants to estimate how many hours per week the average student at Pine Hollow High reads for fun. She stands outside the school library on a Tuesday afternoon and asks the first $75$ students walking out. She reports that the average is about $6.4$ hours per week. Identify the most likely bias source and describe its direction.

Describe the problem with the sampling frame. The reporter only contacted students who had *just left the library*. Students who dislike reading, who never check out books, or who study somewhere else are systematically missing from the pool. The opinions she hears belong entirely to the library-visiting slice of the student body, not to the whole school.

This is a clear case of **selection bias**. The direction of the bias is predictable: library-visiting students are exactly the ones most likely to read heavily, so the sample almost certainly **overestimates** the true reading time for the school as a whole. The "$6.4$ hours" figure may be completely accurate for *library visitors on a Tuesday* but it should not be generalized to "the average student at Pine Hollow High."

A better sampling plan would have pulled names from the full student roster (for example, a stratified random sample across grade levels) and contacted each selected student directly, regardless of where they spent their afternoons.

---

## Example 3: Can the conclusion generalize?

> A company wants to know how their customers feel about a new product. They post a survey link on their official Instagram account and collect $2{,}400$ responses. Among respondents, $84\%$ say they "love" the product. The marketing team announces, "Our customers love the new product." Evaluate whether this conclusion is supported.

Identify what slice of the population actually had a chance of responding. The survey link appeared only to people who (a) follow the company on Instagram, (b) opened the platform during the window the post was live, and (c) cared enough to click through and complete a voluntary form. Those three filters knock out huge segments of the customer base: people who don't use social media, people who follow the company but scrolled past the post, and people who were mildly unhappy but not motivated enough to fill out a form.

This is a double problem. **Selection bias** arises from the recruitment channel itself --- the population of "Instagram followers who saw and clicked the post" is nothing like "all customers." Voluntary-response surveys also suffer from **response bias**, because the people most motivated to reply tend to be the ones with the strongest opinions (in this case, the biggest fans). The sample is systematically tilted toward the product's superfans.

The $84\%$ figure may be perfectly accurate *for Instagram superfans who volunteered to answer*. But the conclusion "our customers love the new product" generalizes well beyond that group, and the sample cannot support it. A defensible study would randomly select customers from the company's order database and contact each one directly (by email or phone), then follow up with non-responders to keep the response rate high.

---

## Common pitfalls

- **Mistaking "big sample" for "good sample."** A convenience sample of $50{,}000$ people can be more biased than a simple random sample of $500$. Size reduces random noise; it does not cancel systematic bias.
- **Confusing stratified with cluster sampling.** In stratified sampling, you draw *some* people from *every* subgroup. In cluster sampling, you take *everybody* from *some* subgroups. The two words sound similar but describe opposite moves.
- **Calling every non-random sample "biased" without naming the source.** On a test question, identify whether the issue is *who* was selected (selection bias) or *what they said* (response bias, including leading questions and non-response).
- **Over-generalizing beyond the sampling frame.** A survey of students at one school supports claims about *that school*, not about all students nationally. Match your conclusion to the actual population you sampled from.
- **Assuming a voluntary-response survey is random.** "Anyone who wants to can answer" is the *opposite* of random. Self-selected respondents are almost always more extreme (pro or con) than the population average.
- **Trusting a single sample point.** Even a well-designed random sample gives an estimate, not a guarantee. Real studies report a **margin of error** to quantify how far the true population value might sit from the sample estimate --- see [[Margin_Of_Error_And_Confidence_Intervals]].

---

## Prerequisites

Before practicing with this page, be comfortable with:

- [[Probability_Of_Simple_And_Compound_Events]] --- sampling methods lean on the language of "chance of being selected"
- [[Mean_Median_Mode_And_Range]] --- so you can interpret what a sample statistic is trying to estimate
- [[Fractions_Decimals_And_Percents]] --- survey results are almost always reported as percentages

---

## Problems Involving Sampling Methods and Bias

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="sampling_methods_and_bias"></div>

---

## See Also

- [[Probability_Of_Simple_And_Compound_Events]]
- [[Histograms_And_Box_Plots]]
- [[Correlation_And_Residuals]]
- [[Scatter_Plots_And_Trend_Lines]]
- [[Margin_Of_Error_And_Confidence_Intervals]]
- [[Mean_Median_Mode_And_Range]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]

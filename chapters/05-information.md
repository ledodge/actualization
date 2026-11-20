# Chapter 5: Information as the Foundation

### Bits, entropy, and why information is physical

---

## The intuition

The earliest version of this framework had a ladder of "dimensions." At the bottom was **information**: pure possibility, before anything happens. Above it was **oscillation**, information interacting with itself. Then **matter**, information that has settled into a definite form. At the top was **continuity**, whatever keeps matter from dissolving back into possibility.

Chapter 2 retired the word "dimension" for this ladder; I now call the rungs **levels**. But the idea that information sits underneath everything has stayed with me. This chapter asks whether physics supports it.

I also had a related idea about the senses. It seemed to me they form a hierarchy by the "density" of what they sense: sight (light, least dense), then sound, smell, taste, and finally touch (solid resistance, most dense). I suspected touch carries the most information, which would explain why we hold on to physical objects to anchor memories. Information theory gives a way to test that, so it's in this chapter too.

---

## The check

### What information is

In 1948 the engineer Claude Shannon gave information a precise definition. Information is a **reduction in uncertainty**. If a coin could land heads or tails and you learn which, you've received one **bit**. If one of eight equally likely outcomes happens, learning which one gives you three bits, because it takes three yes-or-no questions to narrow eight options to one. **[E]**

The amount of uncertainty *before* you learn the answer is called **entropy**. Information is what you gain when entropy goes down. **[E]**

Two more ideas from Shannon's framework matter for this book:

- **Mutual information** measures how much knowing one thing tells you about another. If two variables are completely independent, their mutual information is zero. If knowing one fixes the other, it's as large as it can be. **[E]**
- **Entropy rate** measures how much genuinely new information a process produces per step, information that couldn't have been predicted from everything that came before. **[E]**

### Information is physical

Shannon's definition might sound like it's about messages and telephones, not physics. But in 1961 Rolf Landauer at IBM showed it has a physical cost.

**Landauer's principle:** erasing one bit of information necessarily releases a minimum amount of heat, equal to kT ln 2, where T is the temperature and k is Boltzmann's constant. **[E]** At room temperature that's tiny, about 3 × 10⁻²¹ joules. But it's not zero, and it can't be avoided. Experiments confirmed it directly in 2012 (Bérut et al., *Nature*), measuring the heat released when a single microscopic bead was "erased" from one of two positions.

Landauer's principle also resolved a famous puzzle from 1867, **Maxwell's demon**: a tiny being that sorts fast and slow molecules and seems to beat the second law of thermodynamics. The resolution is that the demon has to record what it sees, and eventually it has to erase those records. The erasure produces at least as much entropy as the sorting removed. **[E]**

Shannon's entropy and the thermodynamic entropy of heat engines turn out to be the same quantity in different units. **[E]**

### "It from bit"

The physicist John Wheeler pushed this idea as far as it can go. In 1989 he proposed "it from bit": the idea that every physical thing ultimately derives its existence from yes-or-no answers, meaning from information. **[P]** That's a philosophical position, not an established result. But it's held by serious physicists, and it's close to what my ladder of levels was reaching for.

### Applying it to the framework

This is where my earlier intuitions get precise forms:

| Original idea | Information-theory version |
|---|---|
| A path has many possible continuations | Its **entropy**: how many continuations remain open |
| A higher observer can see where a path is headed | **Mutual information** between the path's past and its future |
| We can "change direction" unpredictably | A nonzero **entropy rate**: new information that couldn't be forecast |
| Strings influence each other when close | Interacting systems build up **mutual information** (correlation) |

Every entry on the right is measurable. **[E/F]** And they connect to Chapter 4: in a chaotic system, mutual information between the present and the future decays as you look further ahead, and the predictability horizon is roughly where it runs out.

### The senses: my hierarchy was backwards

Now the sense hierarchy. Information theory lets us ask how much information each sense actually carries, and the answer reverses my original claim.

- **Vision** carries by far the most. Each eye sends signals through roughly a million optic nerve fibers, and estimates of the human retina's information rate are on the order of 10 million bits per second. **[E]**
- **Hearing** carries much less, and **touch**, though rich, has lower total bandwidth than vision.
- **Smell and taste** are both chemical senses, so treating them as separate rungs of a "density" ladder doesn't hold up physically.

But one part of the memory intuition survives in a different form. **Smell** has an unusually direct route to the brain's memory and emotion centers: olfactory signals reach the amygdala and hippocampus without first passing through the thalamus, the relay station for the other senses. **[E]** That's widely thought to be why a smell can bring back a memory so vividly. Physical objects help anchor memories because they engage several senses and emotions at once, not because touch is the "densest" channel.

---

## What survives

- **Information is a reduction in uncertainty, measured in bits.** Entropy is the uncertainty that remains. **[E]**
- **Information is physical.** Erasing it has a minimum energy cost, confirmed by experiment. **[E]**
- **My levels idea (information at the bottom) has a serious ancestor** in Wheeler's "it from bit," but it's a philosophical position. **[P]**
- **Paths, predictions, and interactions all have precise information-theoretic versions** using entropy, mutual information, and entropy rate. **[E/F]**
- **My sense hierarchy was wrong:** vision carries the most information, and smell, not touch, has the most direct line to memory. **[E]**

Information is the most solid foundation this framework has. The next three chapters build on it: how possibilities become facts (Chapter 6), why facts stay fixed (Chapter 7), and why time has a direction (Chapter 8).

---

**What would change my mind about this chapter:** a convincing argument that information is derived from physics rather than underlying it, in a way that undercuts the levels idea entirely.

**Further reading:** James Gleick, *The Information*; Charles Seife, *Decoding the Universe*; John Wheeler, "Information, Physics, Quantum: The Search for Links" (1989).

**Discuss this chapter:** [Discussion #5](https://github.com/ledodge/actualization/discussions/5)

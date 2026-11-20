# Chapter 2: Flatland

### What dimensions can and can't do

---

## The intuition

My first pass at this framework was built on dimensions. I'll give it to you close to how I originally wrote it, because most of what's wrong with it is instructive.

Imagine beings who live in fewer dimensions than we do. A **one-dimensional being** lives on a line. It can only move along that line, so it seemed to me that its range of choices was tiny. A **two-dimensional being** lives on a flat plane. It has more freedom than the line-dweller, but it's still limited. **We** live in three dimensions, and three seemed like the minimum you'd need for real diversity: complex decisions, complex movement, complex lives. In a world limited to back-and-forth or side-to-side, I didn't think there could be much variety.

Then I thought about *watching*. A 2D being looking at a 1D being would be able to see far more than the 1D being could, maybe its whole path laid out, past and future at once. We look at 2D things the same way: we draw lines on paper, and from our 3D vantage point we can see where a line is headed and make confident guesses about where it goes, even though it extends forever.

Follow that pattern up one level and you get a **4D being** watching us, perhaps seeing every path we might take and the curve we're currently on. I thought the tricky part was that, even with that view, it might not be able to predict *when* we'd change direction. Our choices would be effectively infinite, and the way our curves overlap and influence each other would be as complicated as the field lines between charged objects placed near each other.

That's the intuition. Almost every sentence of it contains something worth fixing.

---

## The check

### "Number of directions" is the wrong count

A 1D being can actually move in *two* directions: forward and backward. A 2D being can move in *infinitely many* directions: any angle around the compass. So counting directions doesn't capture what I was reaching for.

What I meant is a quantity physicists call **degrees of freedom**: the number of independent numbers you need to describe where something is. A bead on a wire has one. A puck on an air-hockey table has two. A fly in a room has three. **[E]** That's the right measure of "how much room to move" a system has, and it becomes important later in the book. It's not a property of space alone: a system of many particles has many degrees of freedom, even in 3D.

### Three dimensions isn't the minimum for complexity

This was my biggest overreach, and it's simply false as stated.

Very simple rules in very low dimensions can produce enormous complexity. **Conway's Game of Life** is a 2D grid of cells, each either on or off, following four short rules. People have built working computers inside it. Even more striking, **Rule 110**, a *one-dimensional* row of cells with an eight-line update rule, was proven by Matthew Cook (published 2004) to be capable of carrying out any computation a laptop can, given enough space and time. **[E]**

So complexity, in the sense of rich, unpredictable, information-processing behavior, doesn't need three dimensions. A line can do it.

### What three dimensions really do allow

My intuition wasn't completely empty, though. There *are* things that exist in 3D and not in fewer dimensions, and they turn out to be important for life and matter. Here's what survives, in a form I can defend:

**Knots.** In 2D, every closed loop can be smoothly reshaped into a plain circle without cutting it. In 3D, knots exist. In 4D, every knot in a string falls apart, because there's an extra direction to slide strands past each other. Three is the only number of dimensions where a string can tangle permanently. **[E]** (This is mathematics, so it's proven, not just observed.)

**Wiring without crossings.** In 2D, some networks can't be drawn without lines crossing. The simplest examples are five points each connected to every other, or three houses each connected to three utilities. Where lines cross, they'd have to merge. In 3D, *any* network can be built without crossings. Brains, blood vessels, and nervous systems depend on that. **[E]**

**The digestion problem.** In *The Planiverse* (1984), A.K. Dewdney pointed out that a 2D animal with a tube running from mouth to anus would be cut in half by it. Two-dimensional biology needs workarounds, like zippered guts, that 3D life doesn't. **[P/E]** It's a thought experiment, but the geometry behind it is solid.

**Stable orbits and atoms.** In 1917, Paul Ehrenfest showed that if gravity and electric forces work in more than three spatial dimensions the way they work in ours, there are no stable orbits: planets spiral in or fly off. Later work found similar problems for atoms. Three dimensions gives the long-lived structures, like solar systems and atoms, that complex things are made from. **[E/F]**

So the defensible version of "three is the minimum" is narrower but stronger: **three spatial dimensions is the number that allows knotted structure, uncrossed wiring, and stable orbits, all of which complex physical life depends on.** It's not that fewer dimensions can't produce complexity. It's that they can't produce *our kind* of physical complexity.

### Looking from above doesn't show the future

This is the correction that matters most for the rest of the book.

When a 2D being looks at a line, it sees the whole line *in space, at one moment*. That's not the same thing as seeing the line-dweller's past and future. If a point is sliding along a line, someone looking from the side sees where the point is *now*, and the stretch of line it might travel along. They don't see where it has been or where it'll end up unless something records that.

To see a history, you need a different kind of picture. Physicists draw it with one axis for space and another for **time**. A point moving back and forth on a line traces a squiggle on that diagram, and the squiggle *is* its history: every position at every moment, laid out at once. That squiggle is called a **worldline**. **[E]**

The "curve or string" I imagined us traveling on was a worldline all along. But it lives in **spacetime**, not in a fourth spatial dimension. In Einstein's relativity, we are 3D beings whose histories trace worldlines through four-dimensional spacetime, where the fourth dimension is time.

This also changes what a 4D being would see. In Edwin Abbott's *Flatland* (1884), the classic story about dimensions, a 3D sphere visits a 2D world. What the sphere can do is look *inside* closed shapes: into locked rooms and through skin, to see organs. It can't see the future. A being in a fourth *spatial* dimension would relate to us the same way. It could look at our insides from an angle we can't block, but it wouldn't automatically see where we're headed.

### "Seeing all possibilities" is a third kind of space

That leaves one part of my original intuition: a higher observer who sees all the paths we *might* take, but can't know when we'll switch.

That's neither a spatial dimension nor time. It's a **space of possibilities**. Physicists call it **configuration space** when it lists all the arrangements a system could be in, and **phase space** when it includes how fast everything is moving too. A single particle has a 3-dimensional configuration space. A system of a hundred particles has a 300-dimensional one. A brain's is unimaginably large. **[E]**

So in my original intuition, three different things were all being called "dimensions":

| What I said | What it actually is |
|---|---|
| A higher being *looking down* on us | An extra **spatial** dimension (Flatland) |
| Seeing a being's *past and future* | **Time**, giving a worldline in spacetime |
| Seeing *every path we might take* | **Configuration space**, the space of possibilities |

Each is a real and useful idea. Mixing them together is what made my original picture feel profound and also made it incoherent.

### A note on my "dimension" labels

Early versions of this framework also used a dimension ladder in a completely different sense: 1D = information, 2D = oscillation, 3D = matter, 4D = continuity. That wasn't geometry at all. It was a list of *levels* or *layers*, each building on the one below. I still think the layering is worth exploring, and Chapter 5 returns to information as the foundation. But calling the layers "dimensions" made it impossible to discuss them with anyone who uses the word the standard way. From here on I call them **levels**.

---

## What survives

- **Freedom to move is measured in degrees of freedom**, not directions. **[E]**
- **Complexity doesn't require three dimensions.** Even a line can compute anything. **[E]**
- **Three spatial dimensions are special** in a narrower, provable way: knots, uncrossed wiring, and stable orbits. **[E]**
- **The "string" each of us travels is a worldline in spacetime**, and the dimension that holds our past and future is time. **[E]**
- **A higher spatial dimension would let an observer see inside us, not see our future.** Whether such observers exist is a separate question I come back to in Chapter 12, clearly labeled as philosophy. **[P]**
- **"All the paths we could take" lives in configuration space.** That's the idea Chapter 3 builds on: what a higher view of our possibilities would and wouldn't be able to predict, and why the answer depends on chaos, not on dimensions.

The original intuition was a pile of three good ideas wearing one name. Separating them is where the rest of this book starts.

---

**What would change my mind about this chapter:** if there's a meaningful sense in which an extra *spatial* dimension gives access to time that I've missed, or if someone shows the levels idea really does work better as a geometric dimension.

**Further reading:** Edwin Abbott, *Flatland* (1884, public domain); A.K. Dewdney, *The Planiverse* (1984); Ian Stewart, *Flatterland* (2001); any introduction to spacetime diagrams, such as Taylor & Wheeler, *Spacetime Physics*.

**Discuss this chapter:** [Discussion #2](https://github.com/ledodge/actualization/discussions/2)

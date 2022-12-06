# Hospital Supply Distribution
#### Video Demo:  <URL HERE>
#### Description:


##### Building Graph
```mermaid
flowchart TB
    subgraph Building_A
        A0<-->A1
        A1<-->A2
        A2<-->A3
        A3<-->A4
        A4<-->A5
    end
    subgraph Building_B
        B0<-->B1
        B1<-->B2
    end
    subgraph Building_C
        C0<-->C1
        C1<-->C2
        C2<-->C3
    end
    Building_A<-->Building_B
    Building_B<-->Building_C
```
##### Building floor connections
```mermaid
flowchart TB
    A0<-->B0
    B0<-->C0
    A1<-->B1
    B1<-->C1
    B2<-->C2
```
graph TD
    subgraph pipeline[Top level pipeline - pr.yaml]
    A[GitHub Actions Workflow Starts] --> setup
    subgraph setup[telemetry-setup job - shared-actions call]
    C[Load Base Environment Variables global to all jobs]
    C --> D[Stash Variables for Later Use]
    end
    setup --> workflows

    subgraph workflows[Build/test - matrix shared-workflows calls]
    F[Load Stashed Variables]
    F --> G[Run Build/Test Commands]
    G --> H[Add Matrix Attributes, Files]
    H --> I[Stash Job Metadata]
    end

    workflows --> J[All Matrix Jobs Complete]
    subgraph summarize[telemetry-summarize job - shared-actions call]
    L[Parse GitHub Actions Job Metadata]
    L --> M[Associate Jobs with Attributes]
    M --> N[Send Data via OpenTelemetry SDK]
    end
    J --> summarize
    end
    summarize --> O[Vector Forwarder]
    O --> P[Tempo Server<br/>with mTLS Authentication]

    P --> R[TraceQL Queries<br/>Grafana Dashboard]

    style L fill:#e1f5fe
    style M fill:#e1f5fe
    style N fill:#e1f5fe

    style O fill:#fff3e0
    style P fill:#fff3e0
    style R fill:#e8f5e8

    classDef group_headers white-space: nowrap
    class pipeline group_headers
    class summarize group_headers
    class setup group_headers
    class workflows group_headers

    style pipeline fill:#e1f5fe